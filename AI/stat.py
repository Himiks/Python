from statistics import mode
import scipy.stats as stats
import numpy as np
from scipy.stats import ttest_ind

data = [10, 20, 30, 40, 50]
mean = sum(data) / len(data)


sorted_data = sorted(data)
median = sorted_data[len(data)//2] if len(data) % 2 != 0 else\
    (sorted_data[len(data) // 2 - 1] + sorted_data[len(data) // 2]) / 2
    
    
mode(data)

variance = sum((x - mean) ** 2 for x in data) / len(data)
std_deviat = variance ** 0.5

sample_mean = mean
z_score = 1.96
ci = (sample_mean - z_score * (std_deviat / len(data) ** 0.5), sample_mean + z_score * (std_deviat / len(data) ** 0.5 ))


mean = np.mean(data)
variance = np.var(data)
std_dev = np.std(data)

group1 = [10.1, 50.5, 22.8, 33.0, 43.2]
group2 = [5.8, 6.0, 7.4, 87, 9.9]
t_stat, p_value = ttest_ind(group1, group2)

alpha = 0.05

if p_value < alpha:
    print("Reject the null hypothesis: significant difference")
else:
    print("Fails to reject hypothesis: no significant difference")