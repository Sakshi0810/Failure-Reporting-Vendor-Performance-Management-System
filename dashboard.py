import pandas as pd#data analysis
import matplotlib.pyplot as plt#plotting
from matplotlib.ticker import PercentFormatter
g=pd.read_excel('C:/Users/KIIT/Desktop/vendor.xlsx',na_values=['NA'],skipinitialspace=True)
g = g[g.filter(regex='^(?!Unnamed)').columns]

g= g.sort_values(by='defected items',ascending=False)
g["cumpercentage"] = g["defected items"].cumsum()/g["defected items"].sum()*100
fig, ax = plt.subplots(figsize=(20, 10))


ax.bar(g['vendor name'],g['defected items'], color="C0")
ax2 = ax.twinx()
ax2.plot(g['vendor name'],g["cumpercentage"], color="C1", marker="D", ms=7)
plt.setp(ax2.get_xticklabels(), rotation=80, horizontalalignment='right')

ax2.yaxis.set_major_formatter(PercentFormatter())

ax.tick_params(axis="y", colors="C0")
ax2.tick_params(axis="y", colors="C1")
plt.show()


