import matplotlib.pyplot as plt
import numpy as np
x = []
y = []
for t in np.arange(0,9, 0.2):
    x.append(t)
    y.append(np.sin(t))
plt.scatter(x,y)
plt.show()
