#/usr/bin/env python
#
#	RadioactiveDecay.py
#       Python script for UWS first year lab
#       Radioactive Decay experiment
#       James Keatings
#       James.Keatings@uws.ac.uk 
#
#


import numpy as np
import matplotlib.pyplot as plt
import random as rdm

#BEGINING OF THE EXPERIMENT
print("Welcome to the radioactive decay first year lab experiment. In this lab session we will investigate the nature of radioactive decay and observe how it is driven by statistics.")
raw_input("When you are ready to start, please press Enter to continue.")

#Explanation
print("In this experiment we will simulate rolling numerous 6-sided dice with a random number generator. Each dice will represent a nucleus which has a 1 in 6 chance of decaying each unit of time (each dice roll).  If the dice lands on a 1 then we will consider the 'nucleus' has decayed. If we roll the remaining dice and repeat the process we can produce an estimation for how an amount of radioactive material decays over time.")
raw_input("Press Enter to continue when ready.")

#Ask for number of dice
print("How many dice would you like to try rolling? You are required to choose a value greater than 100 and less than 10,000,000.")
while True:
	try:
		number = int(input("Number of dice: "))
	except:
		print("I didn't understand that, please enter a valid number.")
		continue
	if number < 100:
		print("Your value is too low, please enter a value higher than 100.")
		continue
	elif number > 10000000:
		print("Your value is too high, please enter a value lower than 10,000,000.")
		continue
	else:
		print("Thank you, the dice will be rolled " + repr(number) + " times")
		break


#Start rolling
print("\nWe will now begin to roll the dice. After each roll press enter to begin the next one.")
j = 0
points_x = [0]
points_y = [number]
loop_length = 10
sides = 20
sides = 1.0/sides
for i in range(loop_length):
	total = 0
	for j in range(number):
		#if round(rdm.uniform(1,sides),0) == 1:
		if rdm.uniform(0,1) < sides:
			total += 1
	number -= total
	points_x.append(i+1)
	points_y.append(number)
	sum = number + total	
	raw_input("[" + repr(i+1) + "] Out of " + repr(sum) + " remaining nuclei, a total of " + repr(total) + " have decayed and " + repr(number) + " have not.")
	#print("[" + repr(i) + "] Out of " + repr(sum) + " remaining nuclei, a total of " + repr(total) + " have decayed and " + repr(number) + " have not.")

#Draw decay curve
print("\nAll the dice have now been rolled. A graph of the results will now be produced. You will notice it has the shape of am exponential decay.")
p1 = plt.scatter(points_x,points_y, s=50)
plt.show(p1)

#Calculate decay constant
curve_fit = np.polyfit(points_x,np.log(points_y),1)
print(curve_fit)
decay_constant = round(-1/curve_fit[0],3)
#gradient += 0.5
print("Fitting this curve gives a value for the decay constant of " + repr(decay_constant) + " (we rolled a " + repr(1/sides) + " sided dice).")


#END OF THE EXPERIMENT
print("The experiment is now complete.")
