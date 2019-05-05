import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep   # Imports sleep (aka wait or pause) into the program
GPIO.setmode(GPIO.BOARD) # Sets the pin numbering system to use the physical layout
import bluetooth as bt


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
    old_preset = 99
    if preset != old_preset:
        if preset == 0:
            servo_1.ChangeDutyCycle(((1/18)*(0)) + 2.5)
            servo_2.ChangeDutyCycle(((1/18)*(45)) + 2.5)
            servo_3.ChangeDutyCycle(((1/18)*(90)) + 2.5)
            servo_4.ChangeDutyCycle(((1/18)*(135)) + 2.5)
        elif preset == 1:
            servo_1.ChangeDutyCycle(((1/18)*(30)) + 2.5)
            servo_2.ChangeDutyCycle(((1/18)*(60)) + 2.5)
            servo_3.ChangeDutyCycle(((1/18)*(10)) + 2.5)
            servo_4.ChangeDutyCycle(((1/18)*(20)) + 2.5)
        elif preset == 2:
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
    old_preset = preset

server_socket= bt.BluetoothSocket(bt.RFCOMM)
port =1
server_socket.bind(("",port))
server_socket.listen(1)
client,address=server_socket.accept()

while True:
    preset=client.recv(1024)
    print(preset)
    servo(preset)
    
    # Clean up everything

GPIO.cleanup()           # Resets the GPIO pins back to defaults
servo_1.stop()                 # At the end of the program, stop the PWM
servo_2.stop()                 # At the end of the program, stop the PWM
servo_3.stop()                 # At the end of the program, stop the PWM
servo_4.stop()                 # At the end of the program, stop the PWM