import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/gapminder.tsv', sep='\t')

print(type(df))

print(df.shape)

g = df.groupby('year')['lifeExp'].mean()
print(g)
g.plot()
plt.show()
