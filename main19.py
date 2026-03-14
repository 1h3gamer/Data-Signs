import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df=pd.read_csv("heart.csv")
df.head()
df.shape
df.columns
df.describe()
df.isnull().sum()
print(df.info())

df.hist(figsize=(12,12), layout=(5,3))
df.plot(kind="box", subplot=True, layout=(5,3), figsize=(12,12))
plt.show()

sns.barplot(data=df, x="sex", y='chol', hue='target', palette='spring')
df['sex'].value_counts()
df['target'].value_counts()
df['thal'].value_counts()

plt.figure(figsize=(20,10))
sns.heatmap(df.corr(), annot=True, cmap='terrain')

sns.countplot(x='sex',data=df, palette='hsul', hue='target')
sns.countplot(x="target",palette="BuGn",data=df)
sns.countplot(x="ca",hue="target",data=df)