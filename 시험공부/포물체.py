import matplotlib.pyplot as plt
import numpy as np
import math

g = 9.8
v = 37
angle = math.radians(40)
t_flight = 2*v*math.sin(angle)/g
print(t_flight)
def x(t):
    return v*np.cos(angle)*t
def y(t):
    return v*np.sin(angle)*t - 0.5*g*t*t
t = np.arange(0, t_flight, 0.1)
plt.plot(x(t), y(t))
plt.show()
