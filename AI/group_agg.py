import pandas as pd
import numpy as np

data = {
    "Class": ["A", "B", "A", "B", "C", "C"],
    "Score": [85, 90, 95, 75, 95, 80],
    "Age": [15, 16, 15, 17, 16, 15],
}

df = pd.DataFrame(data)

grouped = df.groupby("Class").mean()
# print(grouped)

stats = df.groupby("Class").agg(
    {"Score": ["mean", "max", "min"], "Age": ["mean", "max", "min"]}
)

print(stats)