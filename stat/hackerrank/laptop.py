
import pandas as df
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


df = pd.read_csv("laptop-data.csv",
                 names=["charging_time", "use_time"])

f, ax = plt.subplots()
ax.scatter(df["charging_time"], df["use_time"])
plt.show()
