import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

students = []
preps = []
groups = []
with open("/Users/mikhail/Desktop/python_3sem/laba/lab1/episode_3/data.txt", 'r') as f:
    N = f.readlines()
    f.seek(0)
    for i in N: 
        students.append(f.readline().split(';'))
    for i in range(7):
        x = []
        for j in range(len(N)):
            if str(students[j][0]) == 'prep' + str(i + 1):
                x.append(int(students[j][2]))
        preps.append(x)
    baseline_prep_plot = {} 
    for i in range(7):
        baseline_prep_plot['prep' + str(i + 1)] = 0
    previous_prep_plot = baseline_prep_plot
    fig, ax = plt.subplots()
    for i in range(3, 11):
        prep_plot = {}
        for j in range(7):
            marks = 0
            for k in range(len(preps[j])):
                if i == preps[j][k]:
                    marks += 1
            prep_plot['prep' + str(j + 1)] = marks
        labels = list(prep_plot.keys())
        values = list(prep_plot.values())
        if prep_plot != baseline_prep_plot:   
            ax.bar(labels, values, bottom = list(previous_prep_plot.values()), label = str(i))
        else:
            ax.bar(labels, values, bottom = list(previous_prep_plot.values()))
        for q in range(7):
            previous_prep_plot['prep' + str(q + 1)] += prep_plot['prep' + str(q + 1)]
        ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
        ax.legend(bbox_to_anchor = (0.95, 0.7))
    plt.suptitle("Marks per prep")
    plt.savefig('preps.png', dpi = 1500)
    plt.show()
    for i in range(6):
        x = []
        for j in range(len(N)):
            if str(students[j][1]) == '75' + str(i + 1):
                x.append(int(students[j][2]))
        groups.append(x)
    baseline_group_plot = {} 
    for i in range(6):
        baseline_group_plot['75' + str(i + 1)] = 0
    previous_group_plot = baseline_group_plot  
    for i in range(6):
        previous_group_plot['75' + str(i + 1)] = 0
    fig, ax = plt.subplots()    
    for i in range(3, 11):
        group_plot = {}
        for j in range(6):
            marks = 0
            for k in range(len(groups[j])):
                if i == groups[j][k]:
                    marks += 1
            group_plot['75' + str(j + 1)] = marks
        labels = list(group_plot.keys())
        values = list(group_plot.values())   
        if group_plot != baseline_group_plot:   
            ax.bar(labels, values, bottom = list(previous_group_plot.values()), label = str(i))
        else:
            ax.bar(labels, values, bottom = list(previous_group_plot.values()))
        for q in range(6):
            previous_group_plot['75' + str(q + 1)] += group_plot['75' + str(q + 1)]
        ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
        ax.legend(bbox_to_anchor = (0.95, 0.7))
    plt.suptitle("Marks per group")
    plt.xlabel('group_number')
    plt.savefig('groups.png', dpi = 1500)
    plt.show()
    prep_rating = []
    group_rating = []
    for i in range(7):
        sum = 0 
        for j in range(len(preps[i])):
            sum += float(preps[i][j])
        prep_rating.append(sum/len(preps[i]))
    for i in range(7):
        if prep_rating[i] == max(prep_rating):
            good_prep = i + 1
        if prep_rating[i] == min(prep_rating):
            bad_prep = i + 1
    print("Самый халявный преп №" + str(good_prep))
    print("Самый жесткий преп №" + str(bad_prep))
    for i in range(6):
        sum = 0 
        for j in range(len(groups[i])):
            sum += float(groups[i][j])
        group_rating.append(sum/len(groups[i]))
    for i in range(6):
        if group_rating[i] == min(group_rating):
            bad_group = i + 1
    print("Самая раздолбайская группа: №" + str(bad_group))
    f.close()