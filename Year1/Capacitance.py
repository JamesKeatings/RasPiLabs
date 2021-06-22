#/usr/bin/env python
#
#	Capacitance.py
#       Python script for UWS first year lab
#       Measuring capacitance experiment
#       James Keatings
#       James.Keatings@uws.ac.uk
#       Including scripts based on voltage.py from www.kookye.com
#
#


import time
import RPi.GPIO as GPIO
import sys


#Set up GPIO
AO_pin = 0
SPICKL = 11         #ADC pin 1
SPIMISO = 9         #ADC pin 2
SPIMOSI = 10        #ADC pin 3
SPICS = 8            #ADC pin 4
moswitch_pin = 16    #MOSWITCH pin
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)
GPIO.setup(moswitch_pin, GPIO.OUT)


########################################################################
# FUNCTION DEFINITION COPIED FROM voltage.py FROM www.kookye.com
#read SPI data from MCP3008(or MCP3204) chip,8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        GPIO.output(cspin, True)  

        GPIO.output(clockpin, False)  # start clock low
        GPIO.output(cspin, False)     # bring CS low

        commandout = adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
                if (commandout & 0x80):
                        GPIO.output(mosipin, True)
                else:
                        GPIO.output(mosipin, False)
                commandout <<= 1
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)

        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
                adcout <<= 1
                if (GPIO.input(misopin)):
                        adcout |= 0x1

        GPIO.output(cspin, True)
        adcout >>= 1       # first bit is 'null' so drop it 
        #return adcout      #original line
        return adcout*(3.3/1024)*5  #edited line


########################################################################


#open file to write results to in case of error
f = open("results_capacitance.txt","w")


#BEGINING OF THE EXPERIMENT
print('Welcome to the Capacitance lab experiment. In this experiment you will adjust a variable resistor and observe the affect it has on the time a capacitor takes to discharge.')
input("When you are ready to begin please press Enter to continue.")


#Explanation for stduent
print('\nExplanation goes here bla bla bla.')
input("When you are ready to begin the measurements, please press Enter to continue.")


#Charge the capacitor



#Switch the moswitch to engage the discharge circuit
print('The switch will now disconnect the capacitor from the charging circuit and connect it to the discharging circuit. You will notice that the green LED turns off, and the red LED turns on. As the capacitor discharges the voltage will be printed every 10 seconds.')
input("When you are ready to begin, please press Enter to continue.")
GPIO.output(moswitch_pin,1)

voltage = readadc(AO_pin, SPICLK, SPIMOSI, SPIMISO, SPICS)
print("Voltage = " + str("%.2f"%voltage) + "V")


#END OF THE EXPERIMENT
print('You have now taken all measurements required for this experiment.\nPlease refer to the labscript for the next steps.')

GPIO.cleanup()
sys.exit()
