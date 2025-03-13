import numpy as np

matrix = np.array([[1,2,3], [4,5,6],[7,8,9]])
print("Original matrix\n", matrix)

#Transpose
transpose = matrix.T
print("Transposed\n", transpose)


matrix2 = np.array([[9,8,7], [6,5,4], [3,2,1]])
print("Addition: \n", matrix + matrix2)
print("Multiplication: \n", matrix * matrix2)