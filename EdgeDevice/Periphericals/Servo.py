
import RPi.GPIO as GPIO    #Importamos la libreria RPi.GPIO
import time                #Importamos time para poder usar time.sleep

ServoPin = 38                 # Servo pin 21 - GPIO 20

GPIO.setmode(GPIO.BOARD)   #Ponemos la Raspberry en modo BOARD
GPIO.setup(ServoPin,GPIO.OUT)    #Ponemos el ServoPin como salida
servo = GPIO.PWM(ServoPin, 50)        #Ponemos el ServoPin en modo PWM y enviamos 50 pulsos por segundo
servo.start(7.5)               #Enviamos un pulso del 7.5% para centrar el servo

try:
    while True:      #iniciamos un loop infinito

        servo.ChangeDutyCycle(3.5)    #Enviamos un pulso del 4.5% para girar el servo hacia la izquierda
        time.sleep(0.5)           #pausa de medio segundo
        servo.ChangeDutyCycle(11.5)   #Enviamos un pulso del 10.5% para girar el servo hacia la derecha
        time.sleep(0.5)           #pausa de medio segundo

except KeyboardInterrupt:         #Si el usuario pulsa CONTROL+C entonces...
    servo.stop()                      #Detenemos el servo
    GPIO.cleanup()                #Limpiamos los pines GPIO de la Raspberry y cerramos el script
