import graphviz
import matplotlib.pyplot as plt
import numpy as np
import math

# No. of drones = n = nl * nw (no. of drones in each row * no. of rows)
# Radius of coverage for each drone = rd, Area A = pi * (rd^2)
# Overlapping factor = k, each overlapped area a0 = (k/100) * A
# Ares of coverage for n drones, Ac = (nl * nw * (A - (2*a0)) )
#						+  ( a0 * (nl + nw))

def optDimensions(drone):
	minArea = float("inf")
	nl = 1
	nw = drone 
	for num in range(1, int(math.sqrt(drone)+2)):
		if (drone % num == 0):
			area = ((A - (2*a0)) * drone) + ((num + (drone/num)) * a0)
			print('\t\t',num, ' ', drone/num, ' ', area)
			if area < minArea:
				minArea = area
				nl = num
				nw = drone/num
	print('\t',nl,' ',nw, ' ', minArea)
	return nl, nw

				



k = 10
rd = 500

A = 3.14 * (rd**2)

a0 = (k/100) * A 

n = np.arange(1, 50, 1, int)

print(n)

i = 0
Area = np.ones(n.shape)
Ac = np.ones(n.shape)
for drone in n:
	print(drone,':')
	nl, nw = optDimensions(drone)
	Ac[i] = ((A - (2*a0)) * nl * nw) + ((nl + nw)*a0)
	Area[i] = ((rd*2)*nl)* (nw*(rd*2))
	i = i + 1

fig = plt.plot(n, Ac,'r--', n, Area)

plt.xlabel("No. of drones")
plt.ylabel("Total area of coverage (in sq.m)")
plt.show()
plt.savefig('AvsN1.eps')
plt.close()

