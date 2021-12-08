"""
Exercise on Raspberry Pi Pico/MicroPython
with 480x320 ILI9486 SPI Display
"""
from ili948xnew import ILI9486, color565
from machine import Pin, SPI
from micropython import const
import os
import glcdfont
import tt14
import tt24
import tt32
import time

SCR_WIDTH = const(480)
SCR_HEIGHT = const(320)
SCR_ROT = const(0)
CENTER_Y = int(SCR_WIDTH/2)
CENTER_X = int(SCR_HEIGHT/2)

print(os.uname())
TFT_CLK_PIN = const(2)
TFT_MOSI_PIN = const(3)
TFT_MISO_PIN = const(4)

TFT_CS_PIN = const(1)
TFT_RST_PIN = const(7)
TFT_DC_PIN = const(0)

fonts = [glcdfont]
text = 'Hello Raspberry Pi Pico/ILI9486'

print(text)
print("fonts available:")
for f in fonts:
    print(f.__name__)

spi = SPI(
    0,
    baudrate=16000000,
    polarity=0,
    phase=0,
    bits=16,
    miso=Pin(TFT_MISO_PIN),
    mosi=Pin(TFT_MOSI_PIN),
    sck=Pin(TFT_CLK_PIN))
print(spi)

display = ILI9486(
    spi,
    cs=Pin(TFT_CS_PIN),
    dc=Pin(TFT_DC_PIN),
    rst=Pin(TFT_RST_PIN),
    w=SCR_WIDTH,
    h=SCR_HEIGHT,
    r=SCR_ROT)

display.erase()
display.set_pos(0,0)

#for ff in fonts:
#    display.set_font(ff)
#    display.print(text)
display.fill_rectangle(0, 0, 320, 480, color565(0, 255, 0))    
display.set_font(tt24)
#display.set_color(color565(0, 0, 0), color565(0, 255, 0))
display.print("\nThanks:")
display.print("https://github.com/jeffmer/micropython-ILI9486")

time.sleep(1)

for i in range(170):
    display.scroll(1)
    time.sleep(0.01)
    
time.sleep(1)
for i in range(170):
    display.scroll(-1)
    time.sleep(0.01)
    
time.sleep(5)
display.erase()
display.fill_rectangle(0, 0, 320, 480, color565(255, 0, 0))    
time.sleep(5)
display.erase()
display.fill_rectangle(0, 0, 320, 480, color565(0, 0, 255))    
time.sleep(5)
display.erase()


for h in range(SCR_WIDTH):
    if h > SCR_HEIGHT:
        w = SCR_HEIGHT
    else:
        w = h

    display.fill_rectangle(100, h, 0, h, color565(255, 0, 0))
    time.sleep(0.01)



# Helper function to draw a circle from a given position with a given radius
# This is an implementation of the midpoint circle algorithm,
# see https://en.wikipedia.org/wiki/Midpoint_circle_algorithm#C_example 
# for details
def draw_circle(xpos0, ypos0, rad, col=color565(255, 255, 255)):
    x = rad - 1
    y = 0
    dx = 1
    dy = 1
    err = dx - (rad << 1)
    while x >= y:
        display.pixel(xpos0 + x, ypos0 + y, col)
        display.pixel(xpos0 + y, ypos0 + x, col)
        display.pixel(xpos0 - y, ypos0 + x, col)
        display.pixel(xpos0 - x, ypos0 + y, col)
        display.pixel(xpos0 - x, ypos0 - y, col)
        display.pixel(xpos0 - y, ypos0 - x, col)
        display.pixel(xpos0 + y, ypos0 - x, col)
        display.pixel(xpos0 + x, ypos0 - y, col)
        if err <= 0:
            y += 1
            err += dy
            dy += 2
        if err > 0:
            x -= 1
            dx += 2
            err += dx - (rad << 1)
    


display.set_pos(0,0)
display.print("helloraspberrypi.blogspot.com")

print("Dibuando Circulo Rojo")
for c in range(10):
    draw_circle(CENTER_X, CENTER_Y, c, color565(255, 0, 0))

time.sleep(5)
display.erase()
print("Dibuando Circulo Verde")
for c in range(11):
    draw_circle(CENTER_X, CENTER_Y, c, color565(0, 255, 0))

time.sleep(5)
display.erase()
print("Dibuando Circulo Azul")
for c in range(12):
    draw_circle(CENTER_X, CENTER_Y, c, color565(0, 0, 255))

print("- bye-")