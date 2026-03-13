import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

houseDf = pd.read_csv("USA_Housing.csv")

print("\nFirst 5 rows of the dataset")
print(houseDf.head())

print("\nLast 5 rows of the dataset")
print(houseDf.tail())

print("\nDataset Info")
print(houseDf.info())

print("\nColumn Names")
print(houseDf.columns)

print("\nStatistical Summary")
print(houseDf.isnull().sum())

print("\nMissing values")

sns.pairplot(houseDf)

plt.figure(figsize=(10,6))
sns.heatmap(houseDf.corr(numeric_only=True), annot=True, cmap="coolwarm")

plt.figure()
sns.histplot(houseDf["Price"], bins=30)

plt.show()