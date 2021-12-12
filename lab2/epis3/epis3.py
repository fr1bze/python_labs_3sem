import pandas as pd 
import matplotlib.pyplot as plt
path_res = '/Users/mikhail/Desktop/python_3sem/laba/lab2/epis3/results_ejudge.html'
path_students = '/Users/mikhail/Desktop/python_3sem/laba/lab2/epis3/students_info.xlsx'
results = pd.read_html(path_res)[0].rename(columns={'User': 'login'})
students = pd.read_excel(path_students)
fig, axes = plt.subplots(2, 1,gridspec_kw={"hspace": 0.7}, figsize=[11, 8])

dFrame = pd.merge(students, results, on='login')
x = dFrame.groupby(by = 'group_faculty').mean()['Solved'].plot(kind='bar', ax=axes[0], color = 'blue', xlabel = 'номер факультетских групп')
y= dFrame.groupby(by = 'group_out').mean()['Solved'].plot(kind='bar', ax=axes[1], color ='red', xlabel = 'номер групп по информатике')
data_all_res = dFrame[dFrame['H'] >= 10].groupby(by = 'group_faculty', as_index=False).count()
data_all_res_inf_gr = dFrame[(dFrame['G'] > 10) | (dFrame['H'] > 10)].groupby(by = 'group_out', as_index=False).count()
print(data_all_res.loc[:,['group_faculty', 'H']])
print(data_all_res_inf_gr.loc[:,['group_out', 'H']])
axes[0].set_title('Средняя оценка по факультетским группам')
axes[1].set_title('Средняя оценка по группам для контеста')
axes[0].set_facecolor('seashell')
axes[1].set_facecolor('seashell')
plt.show()
plt.savefig('results.png')