# Set up libraries and overall settings
import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep   # Imports sleep (aka wait or pause) into the program
GPIO.setmode(GPIO.BOARD) # Sets the pin numbering system to use the physical layout

# Set up pin 11 for PWM
GPIO.setup(10,GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
#GPIO.setup(11,GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
#GPIO.setup(12,GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
#GPIO.setup(13,GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
servo_1 = GPIO.PWM(10, 50)     # Sets up pin 11 as a PWM pin
#servo_2 = GPIO.PWM(11, 50)     # Sets up pin 11 as a PWM pin
#servo_3 = GPIO.PWM(12, 50)     # Sets up pin 11 as a PWM pin
#servo_4 = GPIO.PWM(13, 50)     # Sets up pin 11 as a PWM pin
servo_1.start(0)               # Starts running PWM on the pin and sets it to 0
#servo_2.start(0)               # Starts running PWM on the pin and sets it to 0
#servo_3.start(0)               # Starts running PWM on the pin and sets it to 0
#servo_4.start(0)               # Starts running PWM on the pin and sets it to 0

def servo(preset):
    # Move the servo back and forth
    servo_1.start(0)               # Starts running PWM on the pin and sets it to 0
#    servo_2.start(0)               # Starts running PWM on the pin and sets it to 0
#    servo_3.start(0)               # Starts running PWM on the pin and sets it to 0
#    servo_4.start(0)               # Starts running PWM on the pin and sets it to 0

    if preset == 0:
        servo_1.ChangeDutyCycle(((1/180)*(0)) + 1)                      #Move backwards
#        servo_2.ChangeDutyCycle(((1/18)*(45)) + 2.5)
#        servo_3.ChangeDutyCycle(((1/18)*(90)) + 2.5)
#        servo_4.ChangeDutyCycle(((1/18)*(135)) + 2.5)
    elif preset == 1:
        servo_1.ChangeDutyCycle(((1/180)*(90)) + 1)                     #Stop
#        servo_2.ChangeDutyCycle(((1/18)*(60)) + 2.5)
#        servo_3.ChangeDutyCycle(((1/18)*(10)) + 2.5)
#        servo_4.ChangeDutyCycle(((1/18)*(20)) + 2.5)
    elif preset == 2:
        servo_1.ChangeDutyCycle(((1/180)*(180)) + 1)                    #Move forward
#        servo_2.ChangeDutyCycle(((1/18)*(0)) + 2.5)
#        servo_3.ChangeDutyCycle(((1/18)*(90)) + 2.5)
#        servo_4.ChangeDutyCycle(((1/18)*(90)) + 2.5)
#    elif preset == 3:
#        servo_1.ChangeDutyCycle(((1/18)*(60)) + 1)
#        servo_2.ChangeDutyCycle(((1/18)*(100)) + 2.5)
#        servo_3.ChangeDutyCycle(((1/18)*(120)) + 2.5)
#        servo_4.ChangeDutyCycle(((1/18)*(30)) + 2.5)
#    elif preset == 4:
#        servo_1.ChangeDutyCycle(((1/18)*(180)) + 1)
#        servo_2.ChangeDutyCycle(((1/18)*(180)) + 2.5)
#        servo_3.ChangeDutyCycle(((1/18)*(90)) + 2.5)
#        servo_4.ChangeDutyCycle(((1/18)*(0)) + 2.5)
#    sleep(1)
    # Clean up everything


servo(0)
sleep(2)
servo(1)
sleep(2)
servo(2)
sleep(2)
servo(1)
sleep(2)
servo(0)
sleep(2)
servo(1)

GPIO.cleanup()           # Resets the GPIO pins back to defaults
servo_1.stop()                 # At the end of the program, stop the PWM
#servo_2.stop()                 # At the end of the program, stop the PWM
#servo_3.stop()                 # At the end of the program, stop the PWM
#servo_4.stop()                 # At the end of the program, stop the PWM