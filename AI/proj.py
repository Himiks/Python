import numpy as np
from scipy.stats import poisson, norm, binom

np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.rand(100, 1)

X_b = np.c_[np.ones((100,1)), X]
theta = np.random.randn(2, 1)
learning_rate = 0.1
iter = 1000



def predict(X, theta):
    return np.dot(X, theta)


def gradient_descent(X, y, theta, learning_rate, iter):
    m = len(y)
    for _ in range(iter):
        gradients = (1/m) * np.dot(X.T, (np.dot(X, theta) - y))
        theta -=learning_rate * gradients
    return theta


def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred)**2)

def r_squared(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred)**2)
    ss_tot = np.sum((y_true - np.mean(y_true))**2)
    return 1 - (ss_res / ss_tot)