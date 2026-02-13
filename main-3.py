import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

imdb = pd.read_csv('IMDB.csv')

print(imdb.head(3))
print(imdb.shape)
print(imdb.tail(3))
print(imdb.isnull().sum())
print(imdb.describe())
imdb.info()

sns.lineplot(data=imdb, x="Series_Title", y="No_of_Votes")
plt.title("Most votes by Show/Film")
plt.show()

sns.boxplot(data=imdb,x="Runtime", y="IMDB_Rating")
plt.title("Runtime&Rating")
plt.show()

sns.displot(imdb["Runtime"])
plt.title("Runtime distribution")
plt.show()

sns.displot(imdb["IMDB_Rating"])
plt.title("IMDB_Rating Distribution")
plt.show()

sns.countplot(data=imdb, x="Series_Title")
plt.show()