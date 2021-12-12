import pandas as pd

path = '/Users/mikhail/Desktop/python_3sem/laba/lab2/epis1/transactions.csv'
data = pd.read_csv(path, sep = ',').loc[:, 'CONTRACTOR':'SUM'] #исключаем ненужный первый столбец
#print(data)
flex_data = data[data['STATUS'] == 'OK']
print(flex_data.sort_values(by = 'SUM', ascending=False).head(3)) #выводим топ-3 по сумме продаж 
print('\n')
flex_data_new = flex_data[flex_data['CONTRACTOR'] == 'Umbrella, Inc']
print(flex_data_new['SUM'].sum()) #общая сумма продаж Umbrella, Inc