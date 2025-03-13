url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(url)

print(df.info())
print()
print(df.describe())

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

df = df.drop_duplicates()


first_class = df[df["Pclass"] == 1]
print("First class Passangers:\n", first_class)


survival_by_class = df.groupby("Pclass")["Survived"].mean()
survival_by_class.plot(kind="bar", color="skyblue")
plt.title("Survival be class")
plt.ylabel("Survival rate")
plt.show()



sns.histplot(df["Age"], kde=True, bins=20, color="purple")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


plt.scatter(df["Age"], df["Fare"], alpha=0.5, color="green")
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()