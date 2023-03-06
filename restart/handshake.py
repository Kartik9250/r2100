import time
import serial

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.050)
count = 0

while 1:
    ser.write((0xde, 0x01, 0x05, 0x59, 0x83))
    time.sleep(0.1)
    while ser.in_waiting:
        data = ser.readline()
        if len(data)==50:
            data_in=data
            
            print(data_in.hex())
        else:
            pass
        # dist_lsb = data_in[4:-2:4]
        # dist_msb = data_in[5:-2:4]

        # echo_lsb = data_in[6:-2:4]
        # echo_msb = data_in[7:-2:4]

        # print("dist_lsb: ",len(dist_lsb), dist_lsb)
        # print("dist_msb: ",len(dist_msb), dist_msb)
        # print("echo_lsb: ",len(echo_lsb), echo_lsb)
        # print("echo_msb: ",len(echo_msb), echo_msb)
    count += 1

    