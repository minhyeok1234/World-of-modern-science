import matplotlib.pyplot as plt
import numpy as np
x = []
y = []
for t in np.arange(-9,9, 0.5):
    x.append(t)
    y.append(1-t*t)
plt.scatter(x,y)
plt.show()
