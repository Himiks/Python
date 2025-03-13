import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson


lam = 3
x = np.arange(0, 10)
y = poisson.pmf(x, lam)
plt.bar(x, y, color="orange")
plt.title("Poisson dist")
plt.show()