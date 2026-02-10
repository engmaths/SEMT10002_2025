import numpy as np 

predictions = np.array([4, 5, 6, 1, 2, 6, 8, 9, 10])
actual = np.array([5, 5, 6, 2, 3, 5, 4, 7, 9])

#Using vectorised operations to efficiently calculate the MSE
MSE = np.sum((predictions - actual)**2)/predictions.size
print("MSE is", MSE)