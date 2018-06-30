##******************************************************************************
#                           Universidad de Costa Rica
#                  			      IoT_BikeThru
#
# Author: Pablo Avila B30724
# Description: Blink a couple of leds.
#*******************************************************************************

#!/usr/bin/python3

#-------------------- Libraries
import RPi.GPIO as GPIO
import time

#-------------------- Constants and variables
RedLed = 11    # pin11

#-------------------- Setup
def setup():
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(RedLed, GPIO.OUT)   # Set RedLed's mode is output
    GPIO.output(RedLed, GPIO.LOW) # Set RedLed high(+3.3V) to turn on led

#-------------------- Methods
def blink():
    GPIO.output(RedLed, GPIO.HIGH)  # led on
    time.sleep(1)
    GPIO.output(RedLed, GPIO.LOW) # led off
    time.sleep(1)

def destroy():
    GPIO.output(RedLed, GPIO.LOW)   # led off
    GPIO.cleanup()                  # Release resource

##################### MAIN
if __name__ == '__main__':     # Program start from here
    setup()

    #-------------------- Main Loop
    try:
        while True:
            blink()

    #-------------------- Exceptions
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
