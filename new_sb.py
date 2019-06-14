from time import sleep   # Imports sleep (aka wait or pause) into the program
import os 
import bluetooth as bt
import random

intensity_angle = [50, 80, 110, 130, 159, 198, 231]
os.system("echo "+ "P1-11"+ "="+ str(intensity_angle[0]) +"> /dev/servoblaster")
os.system("echo "+ "P1-12"+ "="+ str(intensity_angle[0]) +"> /dev/servoblaster")
os.system("echo "+ "P1-13"+ "="+ str(intensity_angle[0]) +"> /dev/servoblaster")
os.system("echo "+ "P1-15"+ "="+ str(intensity_angle[0]) +"> /dev/servoblaster")
def servo(preset):
    # Move the servo back and forth
    if preset == 1:
        for i in range(intensity_angle[6]+1):
            os.system("echo "+ "P1-11"+ "="+ str(i) +"> /dev/servoblaster")
        for i in range(intensity_angle[3]+1):
            os.system("echo "+ "P1-12"+ "="+ str(i) +"> /dev/servoblaster")
        for i in range(intensity_angle[5]+1):
            os.system("echo "+ "P1-13"+ "="+ str(i) +"> /dev/servoblaster")
        for i in range(intensity_angle[6]+1):
            os.system("echo "+ "P1-15"+ "="+ str(i) +"> /dev/servoblaster")
    elif preset == 2:
        for i in range(intensity_angle[5]+1):
            os.system("echo "+ "P1-11"+ "="+ str(i) +"> /dev/servoblaster")
        for i in range(intensity_angle[4]+1):
            os.system("echo "+ "P1-12"+ "="+ str(i) +"> /dev/servoblaster")
        for i in range(intensity_angle[6]+1):
            os.system("echo "+ "P1-13"+ "="+ str(i) +"> /dev/servoblaster")
        for i in range(intensity_angle[3]+1):
            os.system("echo "+ "P1-15"+ "="+ str(i) +"> /dev/servoblaster")

    elif preset == 3:
        for i in range(intensity_angle[6]+1):
            os.system("echo "+ "P1-11"+ "="+ str(i) +"> /dev/servoblaster")
        for i in range(intensity_angle[2]+1):
            os.system("echo "+ "P1-12"+ "="+ str(i) +"> /dev/servoblaster")
        for i in range(intensity_angle[6]+1):
            os.system("echo "+ "P1-13"+ "="+ str(i) +"> /dev/servoblaster")
        for i in range(intensity_angle[3]+1):
            os.system("echo "+ "P1-15"+ "="+ str(i) +"> /dev/servoblaster")
    elif preset == 4:
        for i in range(intensity_angle[5]+1):
            os.system("echo "+ "P1-11"+ "="+ str(i) +"> /dev/servoblaster")
        for i in range(intensity_angle[1]+1):
            os.system("echo "+ "P1-12"+ "="+ str(i) +"> /dev/servoblaster")
        for i in range(intensity_angle[6]+1):
            os.system("echo "+ "P1-13"+ "="+ str(i) +"> /dev/servoblaster")
        for i in range(intensity_angle[3]+1):
            os.system("echo "+ "P1-15"+ "="+ str(i) +"> /dev/servoblaster")
    elif preset == 5:
        for i in range(intensity_angle[2]+1):
            os.system("echo "+ "P1-11"+ "="+ str(i) +"> /dev/servoblaster")
        for i in range(intensity_angle[0]+1):
            os.system("echo "+ "P1-12"+ "="+ str(i) +"> /dev/servoblaster")
        for i in range(intensity_angle[1]+1):
            os.system("echo "+ "P1-13"+ "="+ str(i) +"> /dev/servoblaster")
        for i in range(intensity_angle[4]+1):
            os.system("echo "+ "P1-15"+ "="+ str(i) +"> /dev/servoblaster")
    
        
server_socket= bt.BluetoothSocket(bt.RFCOMM)
port =1
server_socket.bind(("",port))
server_socket.listen(1)
client,address=server_socket.accept()

while True:
    try:
        preset=client.recv(1024)
        servo(int(preset))
    except:
        server_socket= bt.BluetoothSocket(bt.RFCOMM)
        port =1
        server_socket.bind(("",port))
        server_socket.listen(1)
        client,address=server_socket.accept()
        os.system("echo "+ "P1-11"+ "="+ str(intensity_angle[0]) +"> /dev/servoblaster")
        os.system("echo "+ "P1-12"+ "="+ str(intensity_angle[0]) +"> /dev/servoblaster")
        os.system("echo "+ "P1-13"+ "="+ str(intensity_angle[0]) +"> /dev/servoblaster")
        os.system("echo "+ "P1-15"+ "="+ str(intensity_angle[0]) +"> /dev/servoblaster")
    
# Clean up everything


