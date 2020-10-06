#/usr/bin/env python
#
#	ChaosGame.py
#       Python script for UWS first year lab
#       Chaos Game lab experiment
#       James Keatings
#       James.Keatings@uws.ac.uk
#	

import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt
import time


points_x = [0]
points_y = [0]
circle_x = [0]
circle_y = [0]

#BEGIN EXPERIMENT
print('Welcome to the Monte Carlo Integration lab experiment.')


#Begin random generation
pi_sum = 0
loop_length = 10000
i = 0
loop_number = 10
j = 0
for j in range(loop_number):
	start_time = time.time()
	total = 0
	i = 0
	for i in range(loop_length):
		x = rand.uniform(0,1)
		y = rand.uniform(0,1)
		if (np.sqrt(x**2 + y**2) <= 1.0):
			total += 1
			circle_x.append(x)
			circle_y.append(y)
		else:
			points_x.append(x)
			points_y.append(y)
		
	pi = 4.0 * total/loop_length
	run_time = time.time() - start_time
	print('[' + repr(j) + '] The value of pi for ' + repr(loop_length) + ' iterations is ' + repr(round(pi,6)) + ' (' + repr(round(run_time,3)) + 's)')
	pi_sum += pi
	pi = 0.0
	

#Calculate final pi
pi_final = pi_sum/loop_number
print('\nFinal value of pi = ' + repr(round(pi_final,6)))
print('The actual value of pi is = ' + repr(round(np.pi,6)))
percent_error = round(abs(100 - 100*pi_final/np.pi),4)
print('Your value is ' + repr(percent_error) + '% away from the true value')


#Plot results
area = np.pi*3
colours = (0,0,0)
p1 = plt.scatter(points_x, points_y, s = area)
p1 = plt.scatter(circle_x, circle_y, s = area, c = colours)
plt.xlabel('x')
plt.ylabel('y')
plt.show(p1)

#End experiment
print('The final graph has been produced.\nPlease refer to the labscript for the next steps.\n')
