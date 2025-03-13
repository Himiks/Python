import numpy as np

A = np.array([[1,2], [3,4]])
B = np.array([[5,6], [7,8]])

print(A+B)
print(A-B)

C = 2 * A
print(C)

D = np.dot(A, B)
print(D)

I = np.eye(3)

Z = np.zeros((2,3))

M = np.diad([1, 2, 3])
