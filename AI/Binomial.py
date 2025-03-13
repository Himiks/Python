
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom


n, p = 10, 0.5
x = np.arange(0, n+1)
print(x)
y = binom.pmf(x, n, p)
plt.bar(x, y, color="green")
plt.title("Binomial dist")
plt.show()