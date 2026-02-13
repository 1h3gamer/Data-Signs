import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print(sns.get_dataset_names())

df = sns.load_dataset('penguins')

print(df.head(10))

print(df.shape)

print(df.tail())

print(df.isnull().sum())

print(df.describe())

df.info()

print(df.describe(include="all"))

corr = df.corr(numeric_only=True)
print(corr)

sns.heatmap(corr, cmap="Wistia", annot=True)
plt.show()

df.hist(figsize=(12,8))
plt.show()

df.plot(kind='box',subplots=True, layout=(2,3), sharex=False, sharey=False, figsize=(8,12))
plt.show

print(df['sex'].value_counts())
print(df['island'].value_counts())
print(df['species'].value_counts())

sns.countplot(data=df, x='sex', palette='summer')
plt.show()

sns.countplot(data=df, x='island', palette='RdPu')
plt.show()

sns.countplot(data=df, x='species', palette='YlOrRd')
plt.show()

sns.countplot(data=df, x='sex', hue='species', palette='rocket')
plt.show()

sns.countplot(data=df, x='island', hue='species', palette='husl')
plt.show()

sns.countplot(data=df, x='island', hue='sex', palette='spring')
plt.show()

sns.pairplot(df, hue="species", palette="mako")
plt.show()