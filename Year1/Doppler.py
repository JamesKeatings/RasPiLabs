#/usr/bin/env python
#
#	Doppler.py
#       Python script for UWS first year lab
#       Doppler Shift experiment
#       James Keatings
#       James.Keatings@uws.ac.uk
#
#


import time
import matplotlib.pyplot as plt

#Start experiment
print('Welcome to the Doppler Shift first year lab experiment. In this lab the affect of motion of frequency will be demonstrated.')
raw_input('When you are ready to begin please press Enter to continue.')

#open file to write results to in case of error
f = open("results_doppler.txt","w")

#Explaination of the experiment
print('A sound emitter producing a constant noise is passing a stationary microphone. When the emitter is moving towards the microphone the wavelength of the sound is compressed, and when the emitter is moving away from the microphone the wavelength is stretched. The compression/stretching of the wavelength increases/decreases the frequency of the sound that is heard.')

#Move the emitter
print('The sound emitter will now pass by the microphone at *insert speed here"')

points_x=[0]
pooints_y=[0]


start_time = time.time()
#START EMITTER
#RECORD FREQUENCY FROM MICROPHONE
move_time = round(time.time() - start_time,3)


#Plot graph of results
print('The results have now been recorded and now a graph will displayed showing how the frequency changes over time.')
p1=plt.scatter(points_x, points_y, s=50)
plt.show(p1)

#End experiment
print('You have now taken all measurements required for this experiment.\nPlease refer to the labscript for the next steps.\n')
