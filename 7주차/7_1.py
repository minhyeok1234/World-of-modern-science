import matplotlib.pyplot as plt
import numpy as np

Nt = 1000
x = np.empty(Nt, float)
y = np.empty(Nt, float)
z = np.empty(Nt, float)
x[0] = 0
y[0] = 1
z[0] = 1
dt = 0.001

for i in range(Nt - 1):
    y[i + 1] = dt * z[i] + y[i]
    z[i+1] = dt * y[i] + z[i]
    x[i+1] = x[i] + dt
plt.plot(x, y)
plt.show()
