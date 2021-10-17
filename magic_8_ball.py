# Magic 8 Ball
# This version is stripped down and ready to be uploaded to a Thumby
import time
import thumby
import math
import random

# Create your own sprite here!
# BITMAP: width: 32, height: 32
eight_ball_inv_v7 = (0,0,128,192,224,240,248,252,252,254,254,254,255,255,255,255,255,255,255,255,254,254,254,252,252,248,240,224,192,128,0,0,
            240,254,255,255,255,255,255,255,255,255,255,195,153,60,126,126,126,126,60,153,195,255,255,255,255,255,255,255,255,255,254,240,
            15,127,255,255,255,255,255,255,255,255,255,225,204,158,191,191,191,191,158,204,225,255,255,255,255,255,255,255,255,255,127,15,
            0,0,1,3,7,15,31,63,63,127,127,127,255,255,255,255,255,255,255,255,127,127,127,63,63,31,15,7,3,1,0,0)
# Update this line to use your own sprite here!
my_sprite = eight_ball_inv_v7

# Maximum 9 characters per line
# Up to 5 lines can fit on the screen
# Everything else will get clipped
# Characters may be uppercase letters, lowercase letters, numerals, punctuation and whatever else thumby.display.drawText() supports is valid
# Customize wise messages here!
voodoo_practical = [
    "IT IS\nCERTAIN",
    "IT IS\nDECIDELY\nSO",
    "WITHOUT\nA\nDOUBT",
    "YES\nDEF", # DEFINITELY doesn't fit =/
    "YOU MAY\nRELY\nON IT",
    "AS I\nSEE IT\nYES",
    "MOST\nLIKELY",
    "OUTLOOK\nGOOD",
    "YES",
    "SIGNS\nPOINT TO\nYES",
    "REPLY\nHAZY\nTRY AGAIN",
    "ASK\nAGAIN\nLATER",
    "BETTER\nNOT TELL\nYOU NOW",
    "CANNOT\nPREDICT\nNOW",
    "FOCUS\nAND ASK\nAGAIN", # CONCENTRATE doesn't fit =/
    "DON'T\nCOUNT\nON IT",
    "MY REPLY\nIS\nNO",
    "MY\nSOURCES\nSAY NO",
    "OUTLOOK\nNOT SO\nGOOD",
    "VERY\nDOUBTFUL",
]

# Helper functions:
# Draws up to 3 lines of 9 characters
# Centers each line by padding the string with whitespace. Not perfectly centered
def draw_text(txt : str, x=0, y=0, color=1, force_line_spacing=None, force_y_off=None):
    lines = txt.split('\n')
    
    # offset the entire text drawing depending on how many lines there are
    # space lines apart for readability. Just based off my preference
    if len(lines) == 1:
        y_off = 16
        line_spacing = 0 # Doesn't matter
    elif len(lines) == 2:
        y_off = 9
        line_spacing = 7
    elif len(lines) == 3:
        y_off = 1
        line_spacing = 7
    elif len(lines) == 4:
        y_off = 1
        line_spacing = 3
    elif len(lines) == 5:
        y_off = 0
        line_spacing = 1
    else:
        y_off = 0
        line_spacing = 1
    if force_y_off:
        y_off = force_y_off
    if force_line_spacing:
        line_spacing = force_line_spacing

    for i in range(len(lines)):
        y_off_rel = i * (7 + line_spacing) # relative offset. offset each line from each other so they don't overlap
        thumby.display.drawText(lines[i].center(9), x, y + y_off + y_off_rel, color)

# Copied and modified from TinyBlocks.py
def getcharinputNew():
    if(thumby.buttonL.pressed()):
        return 'L'
    if(thumby.buttonR.pressed()):
        return 'R'
    if(thumby.buttonU.pressed()):
        return 'U'
    if(thumby.buttonD.pressed()):
        return 'D'
    if(thumby.buttonA.pressed()):
        return '1'
    if(thumby.buttonB.pressed()):
        return '2'
    return ' '

# Copied and modified from the default Thumby IDE code
def draw_bobbing_sprite(sprite, sprite_w=32, sprite_h=32, bob_rate=125, bob_range=4):
    # Set arbitrary bob rate (higher is slower)
    # How many pixels to move the sprite up/down (-5px ~ 5px)
    t0 = time.ticks_ms()   # Get time (ms)
    thumby.display.fill(0) # Fill canvas to black

    # Calculate number of pixels to offset sprite for bob animation
    bobOffset = math.sin(t0 / bob_rate) * bob_range

    # Center the sprite using screen and bitmap dimensions and apply bob offset
    spriteX = int((thumby.DISPLAY_W/2) - (32/2))
    spriteY = int(round((thumby.DISPLAY_H/2) - (32/2) + bobOffset))

    # Display the bitmap using bitmap data, position, and bitmap dimensions
    thumby.display.blit(sprite, spriteX, spriteY, sprite_w, sprite_h)
    thumby.display.update()

def draw_idle_view(sprite):
    draw_bobbing_sprite(sprite, bob_rate=250, bob_range=1)

def draw_shaking_ball(sprite):
    draw_bobbing_sprite(sprite, bob_rate=40, bob_range=3)

def magic_eight_ball(sprite):
    shake_threshold_ms = 250 # Must shake at least this long before the venerable ball answers
    idle_threshold_ms = 10000 # This long until the idle animation is shown again
    time_shaken_ms = 0
    time_shaken_start = 0
    time_shaken_end = 0
    time_since_last_shake_ms = None
    is_displaying_msg = False
    is_shaking = False
    while(1):
        c=getcharinputNew()
        any_button_is_pressed = c != ' '
        if any_button_is_pressed:
            is_displaying_msg = False
            if not is_shaking:
                time_shaken_start = time.ticks_ms()
            is_shaking = True
            draw_shaking_ball(sprite)
        elif is_shaking:
            # button was let go
            is_shaking = False # reset the state
            time_shaken_end = time.ticks_ms()
            time_shaken_ms = time_shaken_end - time_shaken_start
            
            # if button let go and it was held long enough (shake_threshold_ms),
            #   show a random message
            # else,
            #   reset to the idle animation
            if time_shaken_ms > shake_threshold_ms:
                is_displaying_msg = True
                rand_int = random.randint(0, len(voodoo_practical)-1)
                thumby.display.fill(0) # Fill canvas to black
                draw_text(voodoo_practical[rand_int])
            else:
                draw_idle_view(sprite)
        elif is_displaying_msg:
            # if no button is pressed, it wasn't just let go, and it's displaying the random message,
            #   check if we should reset to the idle state (idle_threshold_ms)
            # else,
            #   do nothing
            time_since_last_shake_ms = time.ticks_ms() - time_shaken_end
            # Check for idle state
            if time_since_last_shake_ms > idle_threshold_ms:
                is_displaying_msg = False
                time_since_last_shake_ms = None
                draw_idle_view(sprite)
        else:
            # buttons never pressed, idle
            draw_idle_view(sprite)
        thumby.display.update()
        
# Main:
magic_eight_ball(my_sprite)
