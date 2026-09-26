import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("../data/titanic.csv")

print(df.head())

print(df.shape)

print(df.columns)

print(df.info())

print(df.isnull().sum())

print(df.describe())

print(df["Sex"].value_counts())
print(df["Pclass"].value_counts())

print(df.groupby("Sex")["Survived"].mean())
print(df.groupby("Pclass")["Survived"].mean())

df["Sex"].value_counts().plot(kind="bar")
plt.title("Passenger Count by Sex")
plt.xlabel("Sex")
plt.ylabel("Number of Passenger")
#plt.show()

survival_by_sex = df.groupby("Sex")["Survived"].mean()

survival_by_sex.plot(kind="bar")

plt.title("Survival Rate by Sex")
plt.xlabel("Sex")
plt.ylabel("Survival Rate")
plt.ylim(0, 1)
#plt.show()

print(df.groupby(["Pclass", "Sex"])["Survived"].mean())

survival_by_class_sex = df.groupby(["Pclass", "Sex"])["Survived"].mean().unstack()

survival_by_class_sex.plot(kind="bar")

plt.title("Survival Rate by Passenger Class and Sex")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.ylim(0, 1)
plt.legend(title="Sex")
#plt.show()

clean_df = df.copy()

print(df["Age"].median())

clean_df["Age"] = clean_df["Age"].fillna(clean_df["Age"].median())
print(clean_df["Age"].isnull().sum())

print(df["Embarked"].mode())

clean_df["Embarked"] = clean_df["Embarked"].fillna(
    clean_df["Embarked"].mode()[0]
)
print(clean_df["Embarked"].isnull().sum())

print(df["Cabin"].nunique())
print(df["Cabin"].head(20))

print(df["Cabin"].str[0].value_counts())

clean_df["Deck"] = clean_df["Cabin"].str[0].fillna("Unknown")
print(clean_df["Deck"].value_counts())

print(clean_df[["Age", "Embarked", "Deck"]].isnull().sum())

print("Original shape:", df.shape)
print("Cleaned shape:", clean_df.shape)

clean_df.to_csv("../data/titanic_cleaned.csv", index=False)

print(clean_df.isnull().sum())