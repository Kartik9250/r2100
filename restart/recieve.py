import time
import serial

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.050)
count = 0

while 1:
    while ser.in_waiting:
        data_in = ser.readline()
        print(data_in)