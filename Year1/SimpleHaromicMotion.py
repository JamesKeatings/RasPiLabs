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


#open file to write results to in case of error
f = open("results_SimpleHarmonicMotion.txt","w")
#f.write('Goal Temp = ' + repr(goaltemp) +  ' C.\n')
#f.write("Ambient Temp = " + repr(getTemp(ambient)) + ' C.\n')


#BEGINING OF THE EXPERIMENT
print("Welcome to the Simple Haromic Motion first year lab experiment. In this experiment you will investigate the phenomenon known as 'simple harmonic motion' by using an mass suspended from a spring to create a pendulum.")
raw_input("When you are ready to begin please prress Enter to continue.")


#EXPLANATION OF THE EXPERIMENT
print("\nThe mass is moved sideways from its natural resting position (hanging straight down). When the mass is released it will swing back towards the centre due to gravity. The gravitational force causes acceleration towards the resting position, after the pendulum swings past the centre position the mass will start to decelerate due to the force still acting towards the centre. The restorative motion caused by gravity causes the pendulum to oscillate around the centre point.")
raw_input("Press Enter to continue.")


#PLACE THE MASS AT STARTING POSITION
print('\n\Please attach the weight to the electromagnet.')
raw_input("Press Enter to continue.")

print("\nThe weight will now be relased and the period of 20 oscillation recorded.")
print("\nReleaseing the weight in 3......")
time.sleep(1)
print("\n2....")
time.sleep(1)
print("\n1..")
time.sleep(1)
print("\n0!")

#TURN OFF ELECTROMAGNET

#START TIMER WHEN PASSES SWITCH FIRST TIME
start_time=time.time()
i = 0
n = 20
while i < n:
    period = round(time.time() - start_time(),3)
    print("period = " + period + " seconds")
    start_time=time.time()
    i=i+1

#End experiment
print('You have now taken all measurements required for this experiment.\nPlease refer to the labscript for the next steps.\n')
