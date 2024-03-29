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
import RPi.GPIO as GPIO
import sys


#Set up GPIO
button_pin = 10
magnet_pin = 16
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #BUTTON
GPIO.setup(magnet_pin, GPIO.OUT)                            #TRANSISTOR FOR MAGNET

#open file to write results to in case of error
f = open("results_gravity.txt","w")


#define height of set up
height = 1

#BEGINING OF THE EXPERIMENT
print('Welcome to the Gravitional Constant lab experiment.\nIn this lab you will measure the acceleration due to gravity of multiple objects of varying masses, and observe how the acceleration differs.')
input("When you are ready to begin please press Enter to continue.")


#Explanation for stduent
print('\nThere are 3 objects of different masses suspended using an electromagnet. When the current is cut to the magnet the object will fall, after an amount of time it will fall onto a switch. Using the time difference between the begining and end of the fall you will calculate the acceleration due to gravity experienced by the 3 objects.')
input("When you are ready to attach the first object to the magnet, please press Enter")


#Place the ball
print('\nThe magnet is now actived. Please place the ball onto the magnet.')
GPIO.output(magnet_pin, 1)
input('When the metal ball is secured and you are ready to drop, please press enter.')

#Drop and time first object
print('\nThe object will drop in....\n3......')
time.sleep(1)
print('2....')
time.sleep(1)
print('1..')
time.sleep(1)
print('0!')
#turn off magnet
GPIO.output(magnet_pin, 0)
start_time = time.time()

#wait for switch
while True:
	if GPIO.input(button_pin) == GPIO.HIGH:
		print("\nButton pressed!")
		fall_time = round(time.time() - start_time,3)
		break

print('\nThe first object took ' + repr(fall_time) + ' seconds to fall')
acceleration = round(2 * height / fall_time**2,3)
print('For a ' + repr(height) + ' m fall, this gives acceleration equal to ' + repr(acceleration) + ' m/s^2')
f.write("Object 1 = " + repr(fall_time) + " s\n")


#END OF THE EXPERIMENT
print('You have now taken all measurements required for this experiment.\nPlease refer to the labscript for the next steps.')
GPIO.cleanup()
sys.exit()
