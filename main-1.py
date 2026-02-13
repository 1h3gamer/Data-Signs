import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="ticks")

iris = pd.read_csv("Iris.csv")

print(iris.head())
print(iris.info())

sns.barplot(data=iris,x="Species",y="SepalLengthCm")
plt.title("Species & Sepal Length")
plt.show()

sns.boxplot(data=iris,x="Species",y="SepalWidthCm")
plt.title("Species & Sepal Width")
plt.show()

sns.swarmplot(data=iris,x="Species",y="SepalWidthCm")
plt.title("Species & Sepal Width")
plt.show()

sns.countplot(data=iris, x="Species")
plt.show()

sns.displot(iris["SepalWidthCm"])
plt.title("Sepal width Distribution")
plt.show()

sns.jointplot(data=iris, x="SepalWidthCm")
plt.show()

sns.pairplot(data=iris, hue="Species")
plt.title("Species")
plt.show()