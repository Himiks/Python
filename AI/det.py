import numpy as np

A = np.array([[2, 3], [1, 4]])
det = np.linalg.det(A)
# print(det)

inverse = np.linalg.inv(A)
# print(inverse)

eigenVelues, eigneVectors = np.linalg.eig(A)
# print(eigenVelues, eigneVectors)

B = np.array([[4, 2], [1, 2]])

eigval, eigvec = np.linalg.eig(B)


U, S, Vt = np.linalg.svd(A)
print(U, "-----",  S, "---- ", Vt)
