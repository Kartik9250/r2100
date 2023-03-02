import serial
import time
   
ser = serial.Serial(
   port='COM6',
   baudrate=115200,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS
   )

input1 = (0xde, 0x01, 0x05, 0x59, 0x83)
ser.write(input1)

time.sleep(1)
data = []
for i in range(0, 50):
   data.append(ser.read(1).hex())

#print("raw data: ",len(data),data)
#print()
dist_lsb = data[4:-2:4]
dist_msb = data[5:-2:4]

echo_lsb = data[6:-2:4]
echo_msb = data[7:-2:4]
#print("dist_lsb: ",len(dist_lsb), dist_lsb)
#print("dist_msb: ",len(dist_msb), dist_msb)
#print("echo_lsb: ",len(echo_lsb), echo_lsb)
#print("echo_msb: ",len(echo_msb), echo_msb)
#print()
filtered_data = []
for i in range(0,11):
   filtered_data.append([dist_lsb[i], dist_msb[i], echo_lsb[i], echo_msb[i]])
print("filtered data: ", len(filtered_data), filtered_data)
print()

dec_data = []
for i in range(0,11):
   data = []
   for j in range(0,2):
      data.append(int(filtered_data[i][2*j+1]+filtered_data[i][2*j],16))
   dec_data.append(data)

print("Decimal data: ",len(dec_data), dec_data)

   
