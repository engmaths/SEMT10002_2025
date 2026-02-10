import numpy as np

#Make a 3x3 matrix
matrix = np.array([[1, 2, 3], [2, 4, 6], [4, 8, 12]])
print("3x3 matrix\n", matrix)
#Reshape to 1x9
matrix = matrix.reshape((1, 9))
print("1x9 matrix\n", matrix)
matrix = matrix[0, 2:-1]
print("1x6 matrix\n", matrix)
matrix = matrix.reshape((3, 2))
print("3x2 matrix\n", matrix)

#2x2 matrix
matrix = np.array([[7, 9], [4, 6]])
determinant = matrix[0, 0] * matrix[1, 1] - matrix[1, 0] * matrix[0, 1]
print("Determinant of", matrix, "is ", determinant)