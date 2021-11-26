import pandas as pd 
import matplotlib.pyplot as plt
path_res = '/Users/mikhail/Desktop/python_3sem/laba/lab2/epis3/results_ejudge.html'
path_students = '/Users/mikhail/Desktop/python_3sem/laba/lab2/epis3/students_info.xlsx'
results = pd.read_html(path_res)
students = pd.read_excel(path_students)
dFrame = results[0] #изначально это лист из одного элемента
dFrame = dFrame.fillna(0)
#print(dFrame) 
dFrame_score = dFrame[['User', 'Score']]
#print(dFrame_score)
#print(students)
data_all = dFrame.merge(students, left_on= 'User', right_on='login', how='inner')
data = dFrame_score.merge(students, left_on= 'User', right_on='login', how='inner')[['User', 'Score', 'group_faculty', 'group_out']]
#print(data)
data_pre_fac = data.iloc[:,1:3]
data_pre_out = data[['Score','group_out']]
#print(data_pre_out)
data_faculty = data_pre_fac.groupby(by = 'group_faculty', as_index= False).mean()
data_gr_out = data_pre_out.groupby(by = 'group_out', as_index= False).mean()
#print(data_gr_out)
#print(data_faculty)
fig, axes = plt.subplots(2, 1) 
x1 = data_faculty['group_faculty']
x2 = list(data_faculty['Score'])
y1 = data_gr_out['group_out']
y2 = list(data_gr_out['Score'])
axes[0].bar(x1 ,y1,color = 'red', width = 0.5)
axes[1].bar(x2 ,y2,color = 'blue', width = 0.5)
#data_faculty.plot(x = 'group_faculty', y = 'Score', kind = 'bar')
#data_gr_out.plot(x = 'group_out', y = 'Score', kind = 'bar')
fig.set_figwidth(12)
fig.set_figheight(6)
axes[0].set_title('Средняя оценка по факультетским группам')
axes[1].set_title('Средняя оценка по группам для контеста')
axes[0].set_facecolor('seashell')
axes[1].set_facecolor('seashell')
plt.show()
#print(data_all)
data_all_res = data_all[data_all['H'] >= 10].groupby(by = 'group_faculty', as_index=False).count()
data_all_res_inf_gr = data_all[data_all['H'] >= 10].groupby(by = 'group_out', as_index=False).count()
print(data_all_res.loc[:,['group_faculty', 'H']])
print(data_all_res_inf_gr.loc[:,['group_out', 'H']])