##******************************************************************************
#                           Universidad de Costa Rica
#                  			      IoT_BikeThru
#
# Authors:
#   Pablo Avila                 B30724
#   Guido Armas Gonzalez        B30647
#   Felipe Moya Coto            B24609
#   Ricardo Quiros Redondo      B25353
#   Javier Acosta Villalobos    A80056
#
# Description: This is the edge device for auto-rent a bike. If the barcode
# reader detect a valid user, the motor will release the lock an let it that way.
# When a user return the bike, the unique RFID of that bike will be authenticated,
# if it is valid, the motor will lock the bike and ensure the bike stills there
# reading the RFID tag again.
# The red led will always be on unless the barcode reader detects a valid user,
# or the RFID tag is read when returning the bike and is valid. In those cases
# the green led will turn on for 2 seconds and after the red led will turn on again.
#
# Run:
#   sudo ifconfig
#   sudo nmap -sn 192.168.1.0/24
#   scp BikeThru.py pi@192.168.1.18:/home/Documents/UCR/IoT_BikeThru/RUN/
#   ssh pi@192.168.1.18
#   Password:<Password of the Pi>
#   cd /home/Documents/RUN/
#   python BikeThru.py
#*******************************************************************************

#!/usr/bin/python3

#-------------------- Libraries
import sys
sys.path.insert(0, "/home/pi/pi-rc522/ChipReader")
from pirc522 import RFID
import signal
import RPi.GPIO as GPIO
import time
from signal import signal, alarm, SIGALRM
import time


#-------------------- Constants and variables
RedLed = 11                             # pin 11 - GPIO 17
GreenLed = 29                           # pin 29 - GPIO 5
ServoPin = 38                           # Servo pin 21 - GPIO 20
OpenServoDuty = 5
CloseServoDuty = 11

# RFID setup
rdr = RFID()
util = rdr.util()
util.debug = False

# Servo Motor setup
GPIO.setup(ServoPin,GPIO.OUT)           # Set Servo motor pin as output
servo = GPIO.PWM(ServoPin, 50)          # Set Servo motor pin as PWM and 50 pulses per second
servo.start(OpenServoDuty)              # Set pulse width to 7.5% to center the servo

#Alarm setup
signal(SIGALRM, lambda x,y:(1/0))

#-------------------- Setup
def leds_Setup():
    GPIO.setmode(GPIO.BOARD)            # Numbers GPIOs by physical location
    # Red Led
    GPIO.setup(RedLed, GPIO.OUT)        # Set RedLed's mode is output
    GPIO.output(RedLed, GPIO.HIGH)      # Set RedLed high(+3.3V) to turn on led
    # Green Led
    GPIO.setup(GreenLed, GPIO.OUT)      # Set GreenLed's mode is output
    GPIO.output(GreenLed, GPIO.LOW)     # Set GreenLed high(+3.3V) to turn on led

#-------------------- Methods
def returnBike():
    servo.ChangeDutyCycle(CloseServoDuty)# Move servo to 0 degrees
    GPIO.output(GreenLed, GPIO.HIGH)    # Green led on
    GPIO.output(RedLed, GPIO.LOW)       # Red led off
    time.sleep(2)
    GPIO.output(GreenLed, GPIO.LOW)     # Green led off
    GPIO.output(RedLed, GPIO.HIGH)      # Red led on

def rentaBike():
    servo.ChangeDutyCycle(OpenServoDuty)# Move servo to 90 degrees
    GPIO.output(GreenLed, GPIO.HIGH)    # Green led on
    GPIO.output(RedLed, GPIO.LOW)       # Red led off
    time.sleep(2)
    GPIO.output(GreenLed, GPIO.LOW)     # Green led off
    GPIO.output(RedLed, GPIO.HIGH)      # Red led on

def destroy():
    GPIO.output(RedLed, GPIO.LOW)       # Red led off
    GPIO.output(GreenLed, GPIO.LOW)     # Green led off
    servo.stop()                        # Stop the servo
    GPIO.cleanup()

def barcode_read(retry=1 ,wait =1):
  i = 1
  latest_read = ""
  while (i <= retry):                   #Number of desired retries
    try:
      alarm(wait)                       #Calls an alarm to setup a timer for the desired wait for a new stdin
      str = raw_input("Enter your input: ")
      print("Received input is : " + str)
      if (str):
       latest_read = str
    except ZeroDivisionError:
      print("timed out")
    i = i+1
  print("Welcome "+ latest_read)
  return latest_read


##################### MAIN
if __name__ == '__main__':              # Program start from here
    leds_Setup()

    #-------------------- Main Loop
    try:
        while True:
            try:
                #Review if ID input
                ID = barcode_read()
                #Request tag
                (error, data) = rdr.request()

                if (ID != ""):
                    print("New user ID detected:" + ID)
                    rentaBike()
                elif not error:
                    print ("\nNew bike Detected")
                    (error, uid) = rdr.anticoll()
                    if not error:
                         #Print UID
                         print ("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
                         returnBike()
                else:
                    print "No user or bike was detected"
                    GPIO.output(RedLed, GPIO.HIGH)       # Red led off
                    GPIO.output(GreenLed, GPIO.LOW)     # Green led off
                time.sleep(0.7)
            #exception catch required for cases when a newbarcodeID is received during instruction execution other than stin reading
            except ZeroDivisionError:
               print ""

    #-------------------- Exceptions
    # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    except KeyboardInterrupt:
        destroy()
