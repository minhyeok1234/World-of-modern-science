import matplotlib.pyplot as plt

x = [1,3,5,7,9]
y = [2,4,6,8,10]
plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("plot1")

x=[1,2,4,10,13]
y1 = [3,5,6,7,8,9,10]
plt.subplot(1,2,2)
plt.plot(x,y1)
plt.title("plot2")
plt.show()
