import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep   # Imports sleep (aka wait or pause) into the program
GPIO.setmode(GPIO.BOARD) # Sets the pin numbering system to use the physical layout
import bluetooth as bt
import random

# Set up pin 11 for PWM
GPIO.setup(10,GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
GPIO.setup(11,GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
GPIO.setup(12,GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
GPIO.setup(13,GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)


servo_1 = GPIO.PWM(10, 50)     # Sets up pin 11 as a PWM pin
servo_2 = GPIO.PWM(11, 50)     # Sets up pin 11 as a PWM pin
servo_3 = GPIO.PWM(12, 50)     # Sets up pin 11 as a PWM pin
servo_4 = GPIO.PWM(13, 50)     # Sets up pin 11 as a PWM pin
servo_1.start(0)               # Starts running PWM on the pin and sets it to 0
servo_2.start(0)               # Starts running PWM on the pin and sets it to 0
servo_3.start(0)               # Starts running PWM on the pin and sets it to 0
servo_4.start(0)               # Starts running PWM on the pin and sets it to 0

def servo(preset):
    # Move the servo back and forth
    preset = random.randint(0,4)
    if preset == 1:
        servo_1.ChangeDutyCycle(((1/18)*(0)) + 2.5)
        servo_2.ChangeDutyCycle(((1/18)*(45)) + 2.5)
        servo_3.ChangeDutyCycle(((1/18)*(90)) + 2.5)
        servo_4.ChangeDutyCycle(((1/18)*(135)) + 2.5)
    elif preset == 2:
        servo_1.ChangeDutyCycle(((1/18)*(30)) + 2.5)
        servo_2.ChangeDutyCycle(((1/18)*(60)) + 2.5)
        servo_3.ChangeDutyCycle(((1/18)*(10)) + 2.5)
        servo_4.ChangeDutyCycle(((1/18)*(20)) + 2.5)
    elif preset == 0:
        servo_1.ChangeDutyCycle(((1/18)*(0)) + 2.5)
        servo_2.ChangeDutyCycle(((1/18)*(0)) + 2.5)
        servo_3.ChangeDutyCycle(((1/18)*(90)) + 2.5)
        servo_4.ChangeDutyCycle(((1/18)*(90)) + 2.5)
    elif preset == 3:
        servo_1.ChangeDutyCycle(((1/18)*(60)) + 2.5)
        servo_2.ChangeDutyCycle(((1/18)*(100)) + 2.5)
        servo_3.ChangeDutyCycle(((1/18)*(120)) + 2.5)
        servo_4.ChangeDutyCycle(((1/18)*(30)) + 2.5)
    elif preset == 4:
        servo_1.ChangeDutyCycle(((1/18)*(180)) + 2.5)
        servo_2.ChangeDutyCycle(((1/18)*(180)) + 2.5)
        servo_3.ChangeDutyCycle(((1/18)*(90)) + 2.5)
        servo_4.ChangeDutyCycle(((1/18)*(0)) + 2.5)

address=0
server_socket= bt.BluetoothSocket(bt.RFCOMM)
port =1
server_socket.bind(("",port))
print(server_socket.listen(1))
client,address=server_socket.accept()
#print(client)
#print(address)

old = 99
while True:
   #client,address=server_socket.accept()
    print(client)
    print(address)
    print(bt.btcommon.BluetoothError.args)
    try:
        preset=client.recv(1024)
        if preset != old:
            servo(int(preset))
    except:
        server_socket= bt.BluetoothSocket(bt.RFCOMM)
        port =1
        server_socket.bind(("",port))
        print(server_socket.listen(1))
        client,address=server_socket.accept()
    print(preset)
        #old = preset
    
    # Clean up everything


servo_1.stop()                 # At the end of the program, stop the PWM
servo_2.stop()                 # At the end of the program, stop the PWM
servo_3.stop()                 # At the end of the program, stop the PWM
servo_4.stop()                 # At the end of the program, stop the PWM
GPIO.cleanup()           # Resets the GPIO pins back to defaults