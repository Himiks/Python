

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as pllt

df = pd.read_csv(" https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

del df['species']
correlation_matrix = df.corr()

sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
pllt.title("Correlation Heatmap")
pllt.show()