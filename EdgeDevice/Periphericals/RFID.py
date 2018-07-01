##******************************************************************************
#                           Universidad de Costa Rica
#                  			      IoT_BikeThru
#
# Author: Pablo Avila B30724
# Description: Search for RFID or NFC Tags near and displays its UID if found.
#
# Run:
#   sudo ifconfig
#   sudo nmap -sn 192.168.1.0/24
#   scp RFID.py pi@192.168.1.18:/home/Documents/UCR/IoT_BikeThru/RUN/
#   ssh pi@192.168.1.18
#   Password:<Password of the Pi>
#   cd /home/Documents/UCR/IoT_BikeThru/RUN/
#   python RFID.py
#*******************************************************************************

#!/usr/bin/python3

#-------------------- Libraries
import sys
sys.path.insert(0, "/home/pi/pi-rc522/ChipReader")
from pirc522 import RFID
import signal
import time

#-------------------- Setup
rdr = RFID()
util = rdr.util()
util.debug = False

#-------------------- Main Loop
while True:

    #Request tag
    (error, data) = rdr.request()
    if not error:
        print ("\nDetected")
        (error, uid) = rdr.anticoll()
        if not error:
            #Print UID
            print ("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
    time.sleep(1)
