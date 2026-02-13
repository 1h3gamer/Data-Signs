import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="dark")

tips = pd.read_csv("Tips.csv")

sns.scatterplot(data=tips,x="total_bill",y="tip")
plt.title("Total Bill & Tips")
plt.show()

sns.pairplot(data=tips, hue="gender")
plt.title("Gender")
plt.show()

tips.hist(figsize=(12,8))
plt.show()