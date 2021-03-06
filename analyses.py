# IPython log file

import pandas as pd
import matplotlib.pyplot as plt
pd.read_csv('http://www.biostat.jhsph.edu/~rpeng/useRbook/faithful.csv')
df = pd.read_csv('http://www.biostat.jhsph.edu/~rpeng/useRbook/faithful.csv')
df["eruptions"]
df["waiting"]
plt.plot(df["eruptions"], df["waiting"], 'b.')
plt.title("eruptions vs waiting")
plt.savefig("scatter.png")
plt.clf()
plt.hist(df["eruptions"])
plt.title("eruptions")
plt.savefig("eruptions.png")
plt.clf()
plt.hist(df["waiting"])
plt.title("waiting")
plt.savefig("waiting.png")
df.describe().to_csv("stats.txt")


