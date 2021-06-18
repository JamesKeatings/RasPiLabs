#/usr/bin/env python
#
#	Capacitance.py
#       Python script for UWS first year lab
#       Measuring capacitance experiment
#       James Keatings
#       James.Keatings@uws.ac.uk
#
#


import time
import RPi.GPIO as GPIO
import sys


#Set up GPIO
trigger_pin = 16
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(trigger_pin, GPIO.OUT)                            #TRANSISTOR FOR MAGNET

#open file to write results to in case of error
f = open("results_capacitance.txt","w")


#BEGINING OF THE EXPERIMENT
print('Welcome to the Measuring Capacitance lab experiment. In this experiment you will use a variable resister to determine the capactiance of a capacitor in an electrical circuit.')
input("When you are ready to begin please press Enter to continue.")


#Explanation for stduent
print('\nExplanation goes here bla bla bla.')
input("When you are ready to begin the measurements, please press Enter to continue.")


#Change the resistor value
input("\nPlease change the resistor and not down the value. When you are done please press Enter to continue.")


#Charge the capacitor and start a timer


#END OF THE EXPERIMENT
print('You have now taken all measurements required for this experiment.\nPlease refer to the labscript for the next steps.')
sys.exit()
