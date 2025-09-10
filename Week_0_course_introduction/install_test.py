#Import the numpy library
import numpy as np 
#Import the matplotlib library
import matplotlib.pyplot as plt 

xs = np.linspace(0, 100)
ys = np.sin(xs)
plt.plot(xs, ys)
plt.show()