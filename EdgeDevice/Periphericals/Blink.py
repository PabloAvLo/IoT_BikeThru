##******************************************************************************
#                           Universidad de Costa Rica
#                  			      IoT_BikeThru
#
# Authors:
#   Pablo Avila                 B30724
#   Guido Armas González        B30647
#   Felipe Moya Coto            B24609
#   Ricardo Quirós Redondo      B25353
#   Javier Acosta Villalobos    A80056
#
# Description: Blink a couple of leds.
#*******************************************************************************

#!/usr/bin/python3

#-------------------- Libraries
import RPi.GPIO as GPIO
import time

#-------------------- Constants and variables
RedLed = 11    # pin11 - GPIO 17
GreenLed = 29  # pin29 - GPIO 5

#-------------------- Setup
def setup():
    GPIO.setmode(GPIO.BOARD)            # Numbers GPIOs by physical location
    # Red Led
    GPIO.setup(RedLed, GPIO.OUT)        # Set RedLed's mode is output
    GPIO.output(RedLed, GPIO.LOW)       # Set RedLed high(+3.3V) to turn on led
    # Green Led
    GPIO.setup(GreenLed, GPIO.OUT)      # Set GreenLed's mode is output
    GPIO.output(GreenLed, GPIO.LOW)     # Set GreenLed high(+3.3V) to turn on led

#-------------------- Methods
def blink():
    GPIO.output(RedLed, GPIO.HIGH)      # Red led on
    GPIO.output(GreenLed, GPIO.LOW)     # Green led off
    time.sleep(1)
    GPIO.output(RedLed, GPIO.LOW)       # Red led off
    GPIO.output(GreenLed, GPIO.HIGH)    # Green led on
    time.sleep(1)

def destroy():
    GPIO.output(RedLed, GPIO.LOW)       # Red led off
    GPIO.output(GreenLed, GPIO.LOW)     # Green led off
    GPIO.cleanup()                      # Release resource

##################### MAIN
if __name__ == '__main__':              # Program start from here
    setup()

    #-------------------- Main Loop
    try:
        while True:
            blink()

    #-------------------- Exceptions
    # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    except KeyboardInterrupt:
        destroy()
