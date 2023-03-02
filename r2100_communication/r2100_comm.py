import serial
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation
  
class get_Data:
   def __init__(self, ser, request):
      self.ser = ser.write(request)
      self.raw_data = []
      self.filtered_data = []
      self.dec_data = []
      self.dist_lsb = []
      self.dist_msb = []
      self.echo_lsb = []
      self.echo_msb = []

   def raw(self):
      self.raw_data = []
      for i in range(0, 50):
         self.raw_data.append(ser.read(1).hex())
      #print("raw data: ",len(self.raw_data),self.raw_data)
      return(self.raw_data)

   def filtered(self):
      self.raw()
      self.dist_lsb = self.raw_data[4:-2:4]
      self.dist_msb = self.raw_data[5:-2:4]

      self.echo_lsb = self.raw_data[6:-2:4]
      self.echo_msb = self.raw_data[7:-2:4]
      #print("dist_lsb: ",len(self.dist_lsb), self.dist_lsb)
      #print("dist_msb: ",len(self.dist_msb), self.dist_msb)
      #print("echo_lsb: ",len(self.echo_lsb), self.echo_lsb)
      #print("echo_msb: ",len(self.echo_msb), self.echo_msb)
 
      for i in range(0,11):
         self.filtered_data.append([self.dist_lsb[i], self.dist_msb[i], self.echo_lsb[i], self.echo_msb[i]])
         
      #print("filtered data: ", len(self.filtered_data), self.filtered_data)
      return(self.filtered_data)
   
   def decimal(self):
      self.filtered()
      for i in range(0,11):
         data = []
         for j in range(0,2):
            data.append(int(self.filtered_data[i][2*j+1]+self.filtered_data[i][2*j],16))
         self.dec_data.append(data)

      #print("Decimal data: ",len(self.dec_data), self.dec_data)
      return(self.dec_data)      
   
def animate(i):
   get_data = get_Data(ser, request)
   #print("i is", i)
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
   if y1&y2&y3&y4&y5&y6&y7&y8&y10&y11 <= 2000:
      color_val= 'red'
   else:
      color_val = 'blue'
   plt.clf()
   plt.bar([1,2,3,4,5,6,7,8,9,10,11], [y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11], color=color_val)
   
 
   func_data = get_data.decimal()[::-1]
    
if __name__=='__main__':
   #for windows you have to install usb to serial driver
   #windows port = COM6

   #for linux you can check the port by using 'dmesg | grep tty', the port having cp210x is what we have to use
   #port = <connected-port> (usually /dev/ttyUSB0)
   ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
   request = (0xde, 0x01, 0x05, 0x59, 0x83)
   get_data = get_Data(ser, request)
   
   global func_data
   func_data = get_data.decimal()[::-1]

   fig = plt.figure(figsize=(8,6))
   axes = fig.add_subplot(1,1,1)

   plt.title("R2100", color=("blue"))
   ani = FuncAnimation(fig, animate, interval=200,blit=False)

   plt.show()



   # print("1")
   # for i in range (0,11):
   #    x_values.append(i+1)
   #    y_values.append(func_data[i][0])
      
   # plt.bar(x_values, y_values)
   
   # plt.title("R2100")
   # plt.xlabel("Lazers")
   # plt.ylabel("Distance")
   
   # plt.show()
   
