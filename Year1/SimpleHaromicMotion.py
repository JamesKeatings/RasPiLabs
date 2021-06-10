#/usr/bin/env python
#
#	SimpleHarmonicMotion.py
#       Python script for UWS first year lab
#       Simple Harmonic Motion experiment
#       James Keatings
#       James.Keatings@uws.ac.uk
#
#


import os
import glob
import time
import sys
import RPi.GPIO as GPIO


#Definitions
IR_pin = 11
magnet_pin = 16
n = 20
start = 1

#Set up GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(IR_pin, GPIO.IN)
GPIO.setup(magnet_pin, GPIO.OUT)

GPIO.output(magnet_pin,0)

#open file to write results to in case of error
f = open("results_SimpleHarmonicMotion.txt","w")
#f.write('Goal Temp = ' + repr(goaltemp) +  ' C.\n')
#f.write("Ambient Temp = " + repr(getTemp(ambient)) + ' C.\n')


#BEGINING OF THE EXPERIMENT
print("Welcome to the Simple Haromic Motion first year lab experiment. In this experiment you will investigate the phenomenon known as 'simple harmonic motion' by using an mass suspended from a spring to create a pendulum.")
input("When you are ready to begin please prress Enter to continue.")


#EXPLANATION OF THE EXPERIMENT
print("\nThe mass is moved sideways from its natural resting position (hanging straight down). When the mass is released it will swing back towards the centre due to gravity. The gravitational force causes acceleration towards the resting position, after the pendulum swings past the centre position the mass will start to decelerate due to the force still acting towards the centre. The restorative motion caused by gravity causes the pendulum to oscillate around the centre point.")
input("Press Enter to continue.")


#PLACE THE MASS AT STARTING POSITION
print('\nPlease attach the weight to the electromagnet.')
input("Press Enter to continue.")
GPIO.output(magnet_pin,1)


#TURN OFF MAGNET
print("The weight will now be relased and the period of " + repr(n) + " oscillation recorded.")
print("Releaseing the weight in 3......")
time.sleep(1)
print("2....")
time.sleep(1)
print("1..")
time.sleep(1)
print("0!")
GPIO.output(magnet_pin,0)


#START TIMER WHEN PASSES SWITCH FIRST TIME
i = start
total_time = 0
while True:
    if GPIO.input(IR_pin) == GPIO.HIGH:
        print('Starting timing!')
        start_time = time.time()
        time.sleep(1)
        break

#START TIMING EACH PERIOD
while i < n:
    if GPIO.input(IR_pin) == GPIO.HIGH:
        period = round(time.time() - start_time,3)
        start_time=time.time()
        total_time = total_time + period
        print(repr(i) + " :Period = " + repr(period) + " seconds")
        i=i+1
        time.sleep(1)

#RESULTS
average_time = round(total_time/(n-start),3)
print("After " + repr(n-start) + " oscillations, the average time is " + repr(average_time) + ".")

#END EXPERIMENT
print('You have now taken all measurements required for this experiment.\nPlease refer to the labscript for the next steps.\n')
