#/usr/bin/env python
#
#       Fridge & Freezer Temperature Monitor
#                by Tom Caddell
#                    2016
#
# Uses 2 x DS18B20 one-wire temperature sensors (waterproof)


import os
import glob
import time
from RPLCD import CharLCD

#16x2 LCD Display pins 
lcd = CharLCD(cols=16, rows=2, pin_rs=11, pin_e=12, pins_data=[15, 16, 18, 22])


#Create custom degree symbol for LCD - couldn't think of other way to do this!

degree = (
   0b00111,
   0b00101,
   0b00101,
   0b00111,
   0b00000,
   0b00000,
   0b00000,
   0b00000,
)   

lcd.create_char(0, degree)

degree = unichr(0)

#I think this can now be done via raspi-config interface option for 1-wire?
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')


def getTemp(id):
   if id == 'cpu':
      file = open("/sys/class/thermal/thermal_zone0/temp",'r')
      temp = int(file.readline())
   else:
      file = open('/sys/bus/w1/devices/' + id + '/w1_slave', 'r')
      line = file.readline()
      crc = line.rsplit(' ',1)
      crc = crc[1].replace('\n', '')
      if crc=='YES':
         line = file.readline()
         temp = int(line.rsplit('t=',1)[1]) /1000.0
         temp = str(round(temp, 1)) #Round to one decimal place and convert to string
      else:
         temp = 99999
   file.close()
   return temp


#Change address for getTemp to the folder name automatically generated by system for each probe
while True:

 fridge = ("Fridge : " + getTemp('28-8000000480ae') + degree + "C")
 freezer = ("Freezer: " + getTemp('28-8000000481a7') + degree + "C")

 lcd.cursor_pos = (0, 0)
 lcd.write_string(fridge) 
 lcd.cursor_pos = (1, 0)
 lcd.write_string(freezer)
