import pandas as pd
import matplotlib.pyplot as plt

t = pd.read_csv('zillow.csv')

t = t.sort_values(by='ListPrice ($)').reset_index(drop=True)
below200 = 0
over500 = 0
for i in range(len(t)):
    if t['ListPrice ($)'][i] < 200000:
        below200 += 1
    if t['ListPrice ($)'][i] >= 500000:
        over500 += 1
between200and500 = len(t) - below200 - over500
print(t)
print(below200, between200and500, over500)
price = [below200, between200and500, over500]
axes = ['below 200k $', 'between 200k and 500k $', 'over 500k $']
plt.bar(axes, price)
plt.show()
