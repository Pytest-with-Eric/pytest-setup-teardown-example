import re

# Class for Validating IP

class IpCheck:
    
   """
   Check the validity and class of an IP address.

   :Validate_It: Verify the IP address.
   :findClass: Find the class of the IP address.
   """
     
   def __init__(self, IP):
         self.IP = IP
    
   def Validate_It(self):
      # Regex expression for validating IPv4
      regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
      
      # Regex expression for validating IPv6
      regex1 = "((([0-9a-fA-F]){1,4})\\:){7}"\
                      "([0-9a-fA-F]){1,4}"
      
      # Compiling the regex expressions
      p = re.compile(regex)
      p1 = re.compile(regex1)

      # Checking if it is a valid IPv4 address
      if (re.search(p, self.IP)):
         return "Valid IPv4"
      
      # Checking if it is a valid IPv6 address
      elif (re.search(p1, self.IP)):
         return "Valid IPv6"
      
      return "Invalid IP"
    
    # Function to find out the class of an IP address
   def findClass(self):
       ip = self.IP.split(".")
       ip = [int(i) for i in ip]
       
       # If ip >= 0 and ip <= 127 then the IP address is in class A
       if(ip[0] >= 0 and ip[0] <= 127):
          return "A"
   
       # If ip >= 128 and ip <= 191 then the IP address is in class B
       elif(ip[0] >=128 and ip[0] <= 191):
          return "B"
   
       # If ip >= 192 and ip <= 223 then the IP address is in class C
       elif(ip[0] >= 192 and ip[0] <= 223):
          return "C"
   
       # If ip >= 224 and ip <= 239 then the IP address is in class D
       elif(ip[0] >= 224 and ip[0] <= 239):
          return "D"
    
       # Otherwise the IP address is in Class E
       else:
          return "E"
    

# ip = ipCheck("257.120.223.13")

#print(ip.Validate_It())
#print(ip.findClass())