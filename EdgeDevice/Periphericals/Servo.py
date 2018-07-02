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
# Description: Moves the servo Motor to the left, then to the right andd repeat.
#*******************************************************************************

import RPi.GPIO as GPIO
import time

ServoPin = 38                 # Servo pin 21 - GPIO 20

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ServoPin,GPIO.OUT)
servo = GPIO.PWM(ServoPin, 50)
servo.start(7.5)

try:
    while True:
        servo.ChangeDutyCycle(3.5)  # Left
        time.sleep(0.5)
        servo.ChangeDutyCycle(11.5) # Right
        time.sleep(0.5)

except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()
