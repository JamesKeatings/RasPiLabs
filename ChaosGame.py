#/usr/bin/env python
#
#	ChaosGame.py
#       Python script for UWS first year lab
#       Chaos Game lab experiment
#       James Keatings
#       James.Keatings@uws.ac.uk
#	


import random
import matplotlib.pyplot as plt


points_x = [0, 100, 50]
points_y = [100, 100, 0]


#BEGIN EXPERIMENT
print 'Welcome to the Chaos Game lab experiment.'


#Define starting point
#x = random.randint(0,100)
#y = random.randint(0,100)
x=50
y=0
points_x.append(x)
points_y.append(y)


#Run loop
loop_length = 100000
j = 0
while j < loop_length:
	roll = random.randint(0,3)
	x = round((x + points_x[roll])/2,0)
	y = round((y + points_y[roll])/2,0)
	points_x.append(x)
	points_y.append(y)
	j += 1


#Plot results
p1 = plt.scatter(points_x, points_y, s=1)
plt.show(p1)

#End experiment
print 'The final graph has been produced.\nPlease refer to the labscript for the next steps.\n'
