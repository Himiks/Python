import numpy as np

matrix = np.random.randint(1, 51, size=(5, 5))
print("Original:\n", matrix)


print()


matrix[matrix > 25] = 0
print(matrix)


print("Sum:\n", np.sum(matrix))
print("Mean:\n", np.mean(matrix))
print("Standart deviation:\n", np.std(matrix))
