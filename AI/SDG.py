import numpy as np


np.random.seed(42)

X = 2 * np.random.rand(100, 1)
Y = 4 + 3 * X + np.random.randn(100, 1)

X_b = np.c_[np.ones((100, 1)), X]


def stochastic_grad(X, Y, theta, learning_rate, n_epocs):
    m = len(Y)
    for epoch in range(n_epocs):
        for i in range(m):
            random_index = np.random.randint(m)
            xi = X[random_index:random_index+1]
            yi = Y[random_index:random_index+1]
            gradients = 2 * xi.T @ (xi @ theta -yi)
            theta -= learning_rate * gradients
            
    return theta




theta = np.random.rand(2, 1)
learning_rate = 0.01
n_epochs = 50

theta_opt = stochastic_grad(X_b, Y, theta, learning_rate, n_epochs)
print(theta_opt)