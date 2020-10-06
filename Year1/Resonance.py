#/usr/bin/env python
#
#	BiotsLaw.py
#       Python script for UWS first year lab
#       Biot's Law experiment
#       James Keatings
#       James.Keatings@uws.ac.uk
#	Based on fridge.py by Tom Caddell
#
#


import os
import glob
import time


#I think this can now be done via raspi-config interface option for 1-wire?
#os.system('modprobe w1-gpio')
#os.system('modprobe w1-therm')


#def getTemp(id):
#   if id == 'cpu':
#      file = open("/sys/class/thermal/thermal_zone0/temp",'r')
#      temp = int(file.readline())
#   else
#      file = open('/sys/bus/w1/devices/' + id + '/w1_slave', 'r')
#      line = file.readline()
#      crc = line.rsplit(' ',1)
#      crc = crc[1].replace('\n', '')
#      if crc=='YES':
#         line = file.readline()
#         temp = int(line.rsplit('t=',1)[1]) /1000.0
#         temp = round(temp, 1) #Round to one decimal place and convert to string
#      else:
#         temp = 99999
#   file.close()
#   return temp

def getTemp(id):
	return 85

#SET MAX TEMP
goaltemp = 80.0
#SET WATER TEMP ADDRESS
water = '28-8000000480ae'
ambient = '28-8000000480ae'


#open file to write results to in case of error
f = open("results_BiotsLaw.txt","w")
f.write('Goal Temp = ' + repr(goaltemp) +  ' C.\n')
f.write("Ambient Temp = " + repr(getTemp(ambient)) + ' C.\n')


#BEGINING OF THE EXPERIMENT
print("Welcome to the Biot's Law lab experiment.\nIn this lab you will investigate Newton's Law of Cooling by measuring the temperature of a volume of water as it cools and loses heat to the surroundings.")
raw_input("When you are ready to begin please prress Enter to continue.")


#Measure ambient temperature of the room before heating
print('\nWe will take a measurement of the ambient temperature in the room now. Make a note of this value as you will need it to compare with later.')
print('The ambient temperature in the room is ' +  repr(getTemp(ambient)) + ' C')
raw_input("Press Enter to continue.")


#Start heating the water
print('\nWe will now start to heat the water in the container until it reaches ' + repr(goaltemp) + ' C.')
#Turn on USB power
#os.system('uhubctl -a on')
while getTemp(water) < goaltemp:
	print('Current water temp = ' + repr(getTemp(water)))
	time.sleep(1)
#Turn off USB power
#os.system('uhubctl -a off')
print('Heating complete!')


#Measure temperature of water as it cools
print('\nThe water has now reached the desired temperature and will be allowed to cool. The temperature of the water will be printed every minute for an hour, make a record of each value.')
i = 0
while i < 60:
	print('[' + repr(i) + '] Current temperature: ' + repr(getTemp(water)) + ' C.')
	f.write('[' + repr(i) + ']		' + repr(getTemp(water)) + "\n")
	i+=1
	time.sleep(60)


#End experiment
print('You have now taken all measurements required for this experiment.\nPlease refer to the labscript for the next steps.\n')
