import matplotlib.pyplot as plt
import numpy as np

print('sinc 0 is',np.sin(0.0)/0.0)

alpha = np.linspace(-2*np.pi,2*np.pi,100)
plt.plot(alpha,np.sin(alpha)/alpha)
plt.plot(alpha,1-alpha**2/6)
plt.legend(['y=sinc x','$y=1-\\frac{x^2}{6}$'])
plt.savefig('sinc.png')
