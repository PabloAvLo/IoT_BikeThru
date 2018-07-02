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
# Description: Search for RFID or NFC Tags near and displays its UID if found.
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
