import pandas as pd
import matplotlib.pyplot as plt

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
birth_rate = [12,15,11,9,1,9,21]

plt.figure(figsize=(15,9))
plt.bar(days,birth_rate,width=0.8)
plt.xlabel("Days")
plt.ylabel("Birth rate")
plt.title("Birth Rate in July")
plt.legend()
plt.show()