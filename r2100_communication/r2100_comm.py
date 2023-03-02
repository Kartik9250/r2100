import serial
import matplotlib.pyplot as plt
  
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
      print("raw data: ",len(self.raw_data),self.raw_data)
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
         
      print("filtered data: ", len(self.filtered_data), self.filtered_data)
      return(self.filtered_data)
   
   def decimal(self):
      self.filtered()
      for i in range(0,11):
         data = []
         for j in range(0,2):
            data.append(int(self.filtered_data[i][2*j+1]+self.filtered_data[i][2*j],16))
         self.dec_data.append(data)

      print("Decimal data: ",len(self.dec_data), self.dec_data)
      return(self.dec_data)

    
if __name__=='__main__':
   ser = serial.Serial(port='COM6', baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
   request = (0xde, 0x01, 0x05, 0x59, 0x83)
   get_data = get_Data(ser, request)
   
   func_data = get_data.decimal()[::-1]
   x_values = []
   y_values = []
   print("1")
   for i in range (0,11):
      x_values.append(i+1)
      y_values.append(func_data[i][0])
      
   plt.bar(x_values, y_values)
   
   plt.title("R2100")
   plt.xlabel("Lazers")
   plt.ylabel("Distance")
   
   plt.show()
   
