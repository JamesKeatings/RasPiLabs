#/usr/bin/env python
#
#	Gravity.py
#       Python script for UWS first year lab
#       Measuring gravitational constant experiment
#       James Keatings
#       James.Keatings@uws.ac.uk
#
#


import os
import glob
import time

#Function to drop object



#define addresses for objects
object1 = ''
object2 = ''
object3 = ''


#open file to write results to in case of error
f = open("results.txt","w")

#BEGINING OF THE EXPERIMENT
print 'Welcome to the Gravitional Constant lab experiment.\nIn this lab you will measure the acceleration due to gravity of multiple objects of varying masses, and observe how the acceleration differs.\n'
raw_input("When you are ready to begin please press Enter to continue.")


#Explanation for stduent
print 'There are 3 objects of different masses suspended using an electromagnet. When the current is cut to the magnet the object will fall, after an amount of time it will fall onto a switch. Using the time difference between the begining and end of the fall you will calculate the acceleration due to gravity experienced by the 3 objects.\n'
raw_input("When you are ready to drop the first object, please press Enter")


#Drop and time first object
print 'The object will drop in....\n3...'
time.sleep(1)
print '2...\n'
time.sleep(1)
print '1...\n'
time.sleep(1)
print '0!\n'
#turn off magnet
start_time = time.time()
#wait for switch
while not trigger:
	#Check file for trigger
	if :
		trigger = True

fall_time = round(time.time() - start_time,3)

print 'The first object took ' + fall_time + ' seconds to fall'
f.write("Object 1 = " + fall_time + " s\n")

raw_input("When you are ready to drop the second object, please press Enter.")


#drop and time 2nd object



#Drop and time 3rd object




#END OF THE EXPERIMENT
print 'You have now taken all measurements required for this experiment.\nPlease refer to the labscript for the next steps.\n'
