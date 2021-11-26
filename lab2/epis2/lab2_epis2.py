import pandas as pd
import matplotlib.pyplot as plt

path = '/Users/mikhail/Desktop/python_3sem/laba/lab2/epis2/flights.csv'
data = pd.read_csv(path, sep = ',').loc[:, 'CARGO':'WEIGHT'] #исключаем ненужный первый столбец
#print(data)
x = dict(data.groupby(by = 'CARGO').count().loc[:,'PRICE']) #количество перевозок
#print(x)
df = pd.DataFrame(list(x.items()),
                   columns=['CARGO', 'COUNT'])
cargo_data = data.groupby(by = 'CARGO', as_index=False).sum()
df = df.merge(cargo_data, on = 'CARGO')
fig, axes = plt.subplots(3, 1, figsize=(10, 8))
plt.subplots_adjust(wspace=3, hspace= 1)
target1 = [axes[0], axes[1], axes[2]]
df.plot(subplots=True,x = 'CARGO', ax=target1, legend=True, sharex=False, sharey=False, kind = 'bar')
plt.show()
#plt.savefig('fig_epis2.png') #сохранение картинки 