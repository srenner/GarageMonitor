import time
import board
import neopixel
import digitalio
import analogio
import colors

## SETUP #############################################

led = neopixel.NeoPixel(board.NEOPIXEL, 1)

## LOOP ##############################################

while True:
    led.fill(colors.led_red)
    time.sleep(1)
    led.fill(colors.led_green)
    time.sleep(1)
    led.fill(colors.led_blue)
    time.sleep(1)
    led.fill(colors.led_yellow)
    time.sleep(1)
    led.fill(colors.led_white)
    time.sleep(1)
    led.fill(colors.led_off)
    time.sleep(1)
