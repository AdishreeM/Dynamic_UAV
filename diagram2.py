import graphviz
import matplotlib.pyplot as plt
import numpy as np
import math

# No. of drones = n = nl * nw (no. of drones in each row * no. of rows)
# We are taking n = 20 here. Optimal values of nl and nw are 4 and 5. Similarly (5, 6) for 30 and (5, 8) for 40.
# Radius of coverage for each drone = rd, Area A = pi * (rd^2)
# Overlapping factor = k, each overlapped area a0 = (k/100) * A
# Ares of coverage for n drones, Ac = (nl * nw * (A - (2*a0)) ) +  ( a0 * (nl + nw))



k = np.arange(0,100,2,int)

rd = 500

A = 3.14 * (rd**2)

a0 = A/100 * k

nl = [4, 5, 5]
nw = [5, 6, 8]

i = 0
Ac1 = np.ones(k.shape)

for num in k:
	Ac1[i] = ((A - (2*a0[i])) * nl[0] * nw[0]) + ((nl[0] + nw[0])*a0[i])
	print(num, ':\t\t', a0[i], ' ', Ac1[i])
	i = i + 1
i = 0
Ac2 = np.ones(k.shape)

for num in k:
	Ac2[i] = ((A - (2*a0[i])) * nl[1] * nw[1]) + ((nl[1] + nw[1])*a0[i])
	print(num, ':\t\t', a0[i], ' ', Ac2[i])
	i = i + 1
i = 0
Ac3 = np.ones(k.shape)

for num in k:
	Ac3[i] = ((A - (2*a0[i])) * nl[2] * nw[2]) + ((nl[2] + nw[2])*a0[i])
	print(num, ':\t\t', a0[i], ' ', Ac3[i])
	i = i + 1
fig = plt.plot(k, Ac1,'r--', k, Ac2, 'g--', k, Ac3, 'b--')

plt.xlabel("Overlappinf Factor (k)")
plt.ylabel("Total area of coverage (in sq.m)")
plt.show()
plt.close()

