import serial
import time
ser = serial.Serial('/dev/ttyUSB1', 57600, timeout=3 )
time.sleep(2)
command = ''

while True:
    inp = input("Enter the command: ")
    if inp[0] == '8':
        command = 'm 150 150\r\n'
    elif inp[0] == '4':
        command = 'm -150 150\r\n'
    elif inp[0] == '6':
        command = 'm 150 -150\r\n'
    elif inp[0] == '5':
        command = 'm 0 0\r\n'
    elif inp[0] == '2':
        command = 'm -150 -150\r\n'
    elif inp[0] == '7':
        command = 'm 150 75\r\n'
    elif inp[0] == '9':
        command = 'm 75 150\r\n'
    elif inp[0] == '1':
        command = 'm -150 -75\r\n'
    elif inp[0] == '3':
        command = 'm -75 -150\r\n'
    else:
         command = f'{inp}\r\n'

    ser.write(command.encode('utf-8'))
    line = ser.readline()
    print(command, line)