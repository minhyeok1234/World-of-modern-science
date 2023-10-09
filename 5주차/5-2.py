import matplotlib.pyplot as plt
import numpy as np
import math

x = []
g = 9.8
velocity = 37
angle = math.radians(40)
t_flight = 2 * velocity * math.sin(angle)/g
print(t_flight)
for t in np.arange(0, t_flight,(0.1)):
    x.append(velocity*np.cos(angle)*t)
def y(t):
    return velocity * np.sin(angle)*t - 0.5*g*t*t
t = np.arange(0, t_flight,0.1)
plt.plot(x,y(t))
plt.show()
