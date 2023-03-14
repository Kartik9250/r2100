import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import r2100_communication.r2100_comm as r
import serial

def animate(i):
   ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=0.001, write_timeout=0.001)
   request = (0xde, 0x01, 0x05, 0x59, 0x83)
   get_data = r.get_Data(ser, request)
   print("i is", i)
   global func_data
   y1=func_data[0][0]
   y2=func_data[1][0]
   y3=func_data[2][0]
   y4=func_data[3][0]
   y5=func_data[4][0]
   y6=func_data[5][0]
   y7=func_data[6][0]
   y8=func_data[7][0]
   y9=func_data[8][0]
   y10=func_data[9][0]
   y11=func_data[10][0]
   if y1 or y2 or y3 or y4 or y5 or y6 or y7 or y8 or y10 or y11 <= 2000:
      color_val= 'red'
   else:
      color_val = 'blue'
   plt.clf()
   print("clf")
   plt.bar([1,2,3,4,5,6,7,8,9,10,11], [y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11], color=color_val)
   print("bar")
   plt.pause(0.0001)
   func_data = []
   func_data = get_data.decimal_all()[::-1]
   print("func")

def main(z):
   
   if z == True:
      #plt.ion()
      global ser, request
      ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=0.001, write_timeout=0.001)
      request = (0xde, 0x01, 0x05, 0x59, 0x83)
      get_data = r.get_Data(ser, request)

      global func_data
      func_data = get_data.decimal_all()[::-1]

      fig = plt.figure(figsize=(8,6))
      axes = fig.add_subplot(1,1,1)

      plt.title("R2100", color=("blue"))
      ani = FuncAnimation(fig, animate, interval=30)
      fig.show()
      plt.show()

   else:
      print("closing window")
      plt.close('all')

if __name__=='__main__':
   main(True)
