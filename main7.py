import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="ticks")

weather = pd.read_csv("weather.csv")

print(weather.head())
print(weather.info())

sns.barplot(data=weather,x="humidity")
plt.title("Humididty vs Temparature")
plt.show()

sns.displot(weather["humidity"])
plt.title("Humidity Distribution")
plt.show()

sns.displot(weather["humidity"], kde=False, rug=True)
plt.title("Humidity Distribution Without KDE")
plt.show()

sns.jointplot(data=weather, x="humidity", y="temperature", kind="hex")
plt.show()

sns.jointplot(data=weather, x="humidity", y="temperature", kind="kde")
plt.show()

sns.pairplot(weather[["humidity", "temperature", "air_pollution_index"]])
plt.show()

sns.stripplot(data=weather, x="weather type", y="temperature")
plt.show()

sns.barplot(data=weather, x="weather_type", y="temperature", hue="weather_type")
plt.show()

sns.countplot(data=weather, x="weather_type")
plt.show()

sns.pointplot(data=weather, x="weather_type", y="temperature", hue="weather_type")
plt.show()