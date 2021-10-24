# Magic 8 Ball Development version
# This version has a lot of extra stuff for testing and debugging
#
# MIT License
# Copyright (c) 2021 Raymond
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import time
import thumby
import math
import random

# Bitmaps
# BITMAP: width: 32, height: 32
janky_eight_ball = (0,0,128,192,48,16,24,8,12,4,4,2,2,2,3,1,1,1,1,1,1,2,2,4,12,24,112,224,192,128,0,0,
           240,14,3,0,0,0,0,0,128,248,12,6,6,4,228,164,164,228,100,4,4,12,56,224,0,0,0,0,1,3,15,252,
           63,192,0,0,0,0,0,0,31,48,32,96,64,64,192,142,139,137,139,142,128,64,64,96,31,0,0,0,0,0,0,255,
           0,1,6,12,24,48,32,96,64,192,128,128,128,128,128,128,128,128,128,128,128,128,128,64,64,96,32,16,24,4,3,1)

# BITMAP: width: 32, height: 32
eight_ball = (255,255,127,63,31,15,7,3,3,1,1,1,0,0,128,128,128,128,0,0,1,1,1,3,3,7,15,31,63,127,255,255,
           15,1,0,0,0,0,0,192,240,252,254,254,255,207,179,123,123,179,207,255,254,254,252,240,192,0,0,0,0,0,1,15,
           240,128,0,0,0,0,0,3,15,63,127,127,255,249,230,239,239,230,249,255,127,127,63,15,3,0,0,0,0,0,128,240,
           255,255,254,252,248,240,224,192,192,128,128,128,0,0,1,1,1,1,0,0,128,128,128,192,192,224,240,248,252,254,255,255)

# BITMAP: width: 32, height: 32
eight_ball_inv = (0,0,128,192,224,240,248,252,252,254,255,255,255,255,127,127,127,127,255,255,255,255,254,252,252,248,240,224,192,128,0,0,
           240,254,255,255,255,255,255,63,15,3,1,1,0,48,76,132,132,76,48,0,1,1,3,15,63,255,255,255,255,255,254,240,
           15,127,255,255,255,255,255,252,240,192,128,128,0,6,25,16,16,25,6,0,128,128,192,240,252,255,255,255,255,255,127,15,
           0,0,1,3,7,15,31,63,63,127,127,127,255,255,254,254,254,254,255,255,127,127,127,63,63,31,15,7,3,1,0,0)


# BITMAP: width: 32, height: 32
eight_ball_inv_v2 = (0,0,128,192,96,48,24,12,4,6,3,129,129,193,65,65,65,65,193,129,129,3,6,4,12,24,48,96,192,128,0,0,
           240,30,3,0,0,0,224,56,14,3,1,1,0,48,72,136,136,72,48,0,1,1,3,14,56,224,0,0,0,3,30,240,
           15,120,192,0,0,0,7,28,112,192,128,128,0,6,9,8,8,9,6,0,128,128,192,112,28,7,0,0,0,192,120,15,
           0,0,1,3,6,12,24,48,32,96,64,65,193,131,130,130,130,130,131,193,65,64,96,32,48,24,12,6,3,1,0,0)
# BITMAP: width: 32, height: 32
eight_ball_inv_v3 = (0,0,0,128,64,32,16,8,4,4,2,129,129,193,193,193,193,193,193,129,129,2,4,4,8,16,32,64,128,0,0,0,
           224,28,3,0,0,0,224,248,254,255,255,255,255,207,183,119,119,183,207,255,255,255,255,254,248,224,0,0,0,3,28,224,
           7,56,192,0,0,0,7,31,127,255,255,255,255,249,246,247,247,246,249,255,255,255,255,127,31,7,0,0,0,192,56,7,
           0,0,0,1,2,4,8,16,32,32,64,65,65,131,131,131,131,131,131,65,65,64,32,32,16,8,4,2,1,0,0,0)
           
# BITMAP: width: 32, height: 32
eight_ball_inv_v4 = (0,0,0,0,0,0,0,0,0,0,0,0,128,128,128,128,128,128,128,128,0,0,0,0,0,0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,240,248,254,255,255,255,207,183,119,119,183,207,255,255,255,254,248,240,0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,15,31,127,255,255,255,249,246,247,247,246,249,255,255,255,127,63,15,0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0)

# BITMAP: width: 32, height: 32
eight_ball_inv_v5 = (0,0,128,192,224,240,248,252,252,254,254,254,127,127,127,127,127,127,127,127,254,254,254,252,252,248,240,224,192,128,0,0,
           240,254,255,255,255,255,255,255,255,255,193,156,62,127,127,127,127,127,127,62,156,193,255,255,255,255,255,255,255,255,254,240,
           15,127,255,255,255,255,255,255,255,255,193,156,62,127,127,127,127,127,127,62,156,193,255,255,255,255,255,255,255,255,127,15,
           0,0,1,3,7,15,63,63,127,127,127,127,255,255,255,255,255,255,255,255,127,127,127,63,63,31,15,7,3,1,0,0)

# BITMAP: width: 32, height: 32
eight_ball_inv_v6 = (0,0,128,192,224,240,248,252,252,254,254,254,255,255,255,255,255,255,255,255,254,254,254,252,252,248,240,224,192,128,0,0,
            240,254,255,255,255,255,255,255,255,255,255,195,153,60,126,126,126,126,60,153,195,255,255,255,255,255,255,255,255,255,254,240,
            15,127,255,255,255,255,255,255,255,255,255,225,204,158,191,191,191,191,158,204,225,255,255,255,255,255,255,255,255,255,127,15,
            0,0,1,3,7,15,63,63,127,127,127,127,255,255,255,255,255,255,255,255,127,127,127,63,63,31,15,7,3,1,0,0)

# BITMAP: width: 32, height: 32
eight_ball_inv_v7 = (0,0,128,192,224,240,248,252,252,254,254,254,255,255,255,255,255,255,255,255,254,254,254,252,252,248,240,224,192,128,0,0,
            240,254,255,255,255,255,255,255,255,255,255,195,153,60,126,126,126,126,60,153,195,255,255,255,255,255,255,255,255,255,254,240,
            15,127,255,255,255,255,255,255,255,255,255,225,204,158,191,191,191,191,158,204,225,255,255,255,255,255,255,255,255,255,127,15,
            0,0,1,3,7,15,31,63,63,127,127,127,255,255,255,255,255,255,255,255,127,127,127,63,63,31,15,7,3,1,0,0)


# Spaces and new lines based on the real thing
# https://www.reddit.com/r/mildlyinteresting/comments/39zg4p/comment/cs7uv3k/?utm_source=share&utm_medium=web2x&context=3
voodoo = [
    "IT  IS\nCERTAIN",
    "IT IS\nDECIDELY\nSO",
    "WITHOUT\nA\nDOUBT",
    "YES\nDEFINITELY",
    "YOU MAY\nRELY\nON IT",
    "AS  I\nSEE IT\nYES",
    "MOST\nLIKELY",
    "OUTLOOK\nGOOD",
    "YES",
    "SIGNS\nPOINT TO\nYES",
    "REPLYHAZY\nTRY\nAGAIN", # Yes, there's no visible space between reply and hazy
    "ASK\nAGAIN\nLATER",
    "BETTERNOT\nTELL YOU\nNOW", # Combined BETTER and NOT so it fits 9 characters
    "CANNOT\nPREDICT\nNOW",
    "CONCENTRATE\nAND ASK\nAGAIN", # Sad this doesn't fit the default font
    "DON'T\nCOUNT\nON  IT",
    "MY REPLY\nIS\nNO",
    "MY\nSOURCES\nSAY\nNO",
    "OUTLOOK\nNOT  SO\nGOOD",
    "VERY\nDOUBTFUL",
]

voodoo_practical = [
    "IT IS\nCERTAIN",
    "IT IS\nDECIDELY\nSO",
    "WITHOUT\nA\nDOUBT",
    "YES\nDEF",
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
    "FOCUS\nAND ASK\nAGAIN",
    "DON'T\nCOUNT\nON IT",
    "MY REPLY\nIS\nNO",
    "MY\nSOURCES\nSAY NO",
    "OUTLOOK\nNOT SO\nGOOD",
    "VERY\nDOUBTFUL",
]

# Helper functions:
# Draws up to 3 lines of 9 characters
# Centers each line
def draw_text(txt : str, x=0, y=0, color=1):
    lines = txt.split('\n')
    for i in range(len(lines)):
        y_off = i*15
        if len(lines) == 1:
            y_off += 15
        elif len(lines) == 2:
            y_off += 8
        elif len(lines) == 3:
            y_off += 1
        thumby.display.drawText(lines[i].center(9), x, y + y_off, color)

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

# Copied from the default Thumby IDE code
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
            # thumby.display.update()
        elif is_shaking:
            # button let go
            is_shaking = False
            time_shaken_end = time.ticks_ms()
            time_shaken_ms = time_shaken_end - time_shaken_start
            
            # if button let go and it was held long enough, 
            if time_shaken_ms > shake_threshold_ms:
                is_displaying_msg = True
                rand_int = random.randint(0, len(voodoo_practical)-1)
                thumby.display.fill(0) # Fill canvas to black
                draw_text(voodoo_practical[rand_int])
            else:
                draw_idle_view(sprite)
        elif is_displaying_msg:
            time_since_last_shake_ms = time.ticks_ms() - time_shaken_end
            # Check for idle state
            if time_since_last_shake_ms > idle_threshold_ms:
                is_displaying_msg = False
                time_since_last_shake_ms = None
                draw_idle_view(sprite)
        else:
            # buttons never pressed
            draw_idle_view(sprite)
        thumby.display.update()
        
# Main:
magic_eight_ball(eight_ball_inv_v7)

# Test functions:
def test_all_messages():
    for msg in voodoo_practical:
        thumby.display.fill(0) # Fill canvas to black
        time.sleep(1)
        draw_text(msg, 0, 0)
        thumby.display.update()
        time.sleep(1)

def test_rng():
    for i in range(20):
        rand_int = random.randint(0, len(voodoo_practical)-1)
        # rand_int = random.randint(0, 2)
        thumby.display.fill(0) # Fill canvas to black
        time.sleep(1)
        draw_text(str(rand_int))
        thumby.display.update()
        time.sleep(1)

def test_rng_msg():
    for i in range(20):
        rand_int = random.randint(0, len(voodoo_practical)-1)
        thumby.display.fill(0) # Fill canvas to black
        time.sleep(1)
        draw_text(voodoo_practical[rand_int])
        thumby.display.update()
        time.sleep(1)

def test_input():
    while(1):
        c=getcharinputNew()
        if c != ' ':
            thumby.display.fill(0) # Fill canvas to black
            draw_text(c)
            thumby.display.update()
        else:
            # thumby.display.fill(0)
            pass
        time.sleep(0.25)

def test_animations():
    while(1):
        # draw_idle_view()
        draw_shaking_ball()
