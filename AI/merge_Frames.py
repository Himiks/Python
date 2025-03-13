import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    "ID": [1,2,3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
})

df2 = pd.DataFrame({
    "ID": [1,2,3],
    "Score": [85, 90, 95],
})

# print(df1)
# print()
# print(df2)

merged = pd.merge(df1, df2, how="inner", on="ID")


print(merged)
merged["Score_Percentage"] = (merged["Score"] / 100) * 100

print()
print(merged)