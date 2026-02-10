import numpy as np

coefficients = np.array([1, -2, 1])
solution = np.roots(coefficients)
print("Solution 1: ", solution)

coefficients = np.array([np.random.random() for val in range(1000)])
solution = np.roots(coefficients)
print("Solution 2: ", solution)