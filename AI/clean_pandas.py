import pandas as pd
import numpy as np

data = {
    "Name": ["Alice", "Bob", np.nan, "David"],
    "Age": [25, np.nan, 30, 35],
    "Score": [85, 90, np.nan, 88],
}

df = pd.DataFrame(data)
# print(df)

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Score"] = df["Score"].interpolate()

# print(df)

df = df.rename(columns={"Name": "Student_Name", "Score":"Exam_Score"})
print(df)