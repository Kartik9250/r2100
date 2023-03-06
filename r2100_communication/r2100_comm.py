# While making the class object you must pass the following parameters: 
# ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)

#for windows you have to install usb to serial driver
#windows port = COM6

#for linux you can check the port by using 'dmesg | grep tty', the port having cp210x is what we have to use
#port = <connected-port> (usually /dev/ttyUSB0)

# request = (0xde, 0x01, 0x05, 0x59, 0x83)
# get_data = get_Data(ser, request)

class get_Data:
   def __init__(self, ser, request):
      self.ser = ser
      self.raw_data = []
      self.filtered_data = []
      self.dist_lsb = []
      self.dist_msb = []
      self.echo_lsb = []
      self.echo_msb = []

      self.dec_all = []
      self.dec_dist = []
      self.dec_echo = []


      self.ser.write(request)

   def raw(self):
      self.raw_data = []
      for i in range(0, 50):
         self.raw_data.append(self.ser.read(1).hex())
      #print("raw data: ",len(self.raw_data),self.raw_data)
      return self.raw_data

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
      return self.filtered_data
   
   def decimal_all(self):
      self.filtered()
      for i in range(0,11):
         data = []
         for j in range(0,2):
            data.append(int(self.filtered_data[i][2*j+1]+self.filtered_data[i][2*j],16))
         self.dec_all.append(data)

      #print("All decimal data: ",len(self.dec_all), self.dec_all)
      return self.dec_all

   def decimal_dist(self):
      data = self.decimal_all()
      print(data)

      for i in data:
         self.dec_dist.append(i[0])
      #print("Decimal distance data: ",len(self.dec_dist), self.dec_dist)
      return self.dec_dist
   

   def decimal_echo(self):
      data = self.decimal_all()

      for i in data:
         self.dec_dist.append(i[1])
      #print("Decimal echo data: ",len(self.dec_echo), self.dec_echo)
      return self.dec_dist
    
