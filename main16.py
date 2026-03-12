import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

penguins_df = pd.read_csv('Penguins Data.csv')
penguins = penguins_df
penguins.head(3)

x=penguins.get("studyName")
y=penguins.get("Culmen_Length_(mm)")

type=[x,y]
colors=['y','r']
label = ['Name','Culmen Length']
bins = [30,35,40,45]
plt.xlabel("Study Name")
plt.ylabel("Culmen Length(mm)")

plt.hist(type, bins=bins, rwidth=0.95, color=colors, label=label, orientation="horizontal")

plt.title("Culmen length and name")
plt.legend()
plt.show()