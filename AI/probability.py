import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson, norm, binom



def bayes_theory(prior, sensetivity, specificity):
    evidence = (sensetivity * prior) + ((1-specificity) * (1-prior))
    posterior = (sensetivity * prior) / evidence
    return posterior


prior = 0.01
sensitivity = 0.95
specificity = 0.90

print(bayes_theory(prior, sensitivity, specificity))



x = np.linspace(-4, 4, 100)
y = norm.pdf(x, loc=0, scale=1)
plt.plot(x, y, label="Gaussian")
plt.title("Gaussian")
plt.show()


