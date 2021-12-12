import pandas as pd
import matplotlib.pyplot as plt

path = '/Users/mikhail/Desktop/python_3sem/laba/lab2/epis2/flights.csv'
data = pd.read_csv(path) #исключаем ненужный первый столбец

fig, axes = plt.subplots(3, 1, figsize=(10, 10))
data.groupby('CARGO').count()['Unnamed: 0'].plot(kind='bar', ax=axes[0], title='Amount of flights')
data.groupby('CARGO').sum()['PRICE'].plot(kind='bar', ax=axes[1], title='Price', color = 'orange')
data.groupby('CARGO').sum()['WEIGHT'].plot(kind='bar', ax=axes[2], title='Weight', color = 'green')
plt.show()
#plt.savefig('fig_epis2.png') #сохранение картинки 