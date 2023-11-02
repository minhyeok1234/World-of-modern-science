import matplotlib.pyplot as plt
import numpy as np

g = 9.8
v0 = 37

def velocity(t):
    return v0 - g * t

dt = 0.01
g = 9.8
timeEnd = 7.7
Nt = (int)(timeEnd/dt) + 1

yList = np.empty(Nt, float)
tList = np.empty(Nt, float)

yList[0] = 0
tList[0] = 0

for n in range(Nt - 1):
    yList[n+1] = yList[n] + dt * velocity(tList[n]) - 1/3 * yList[n] * yList[n]
    tList[n+1] = tList[n] + dt
print(Nt)
plt.plot(tList, yList)
plt.show()
