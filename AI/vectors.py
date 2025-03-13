import numpy as np

M = np.array([[1,2, 3], [4, 5,6], [7,8,9]])
v = np.array([1, 0, -1])

result = np.dot(M, v)
print(result)


I = np.eye(3)
A = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(np.dot(A, I))


D = np.diag([1,7,9])
Z = np.zeros((3, 3))
