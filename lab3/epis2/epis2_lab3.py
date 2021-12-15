from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
#path1 = '/Users/mikhail/Desktop/python_3sem/laba/lab3/epis2/signal01.dat'
#path2 = '/Users/mikhail/Desktop/python_3sem/laba/lab3/epis2/signal02.dat'
#path3 = '/Users/mikhail/Desktop/python_3sem/laba/lab3/epis2/signal03.dat'
#print(a1[1:10])
def running_mean(x, n = 5):
    arr = np.zeros(x.shape,dtype = float)
    cumsum = np.cumsum(x) 
    #arr[:n] = cumsum[:n] / np.arange(1, n + 1)
    arr[-n:] = cumsum[-n:] / np.arange(x.shape[0], x.shape[0] - int(n), -1)
    arr[:n] = cumsum[:n] / np.arange(1, n+1)
    arr[n:-n] = (cumsum[n:-n] - cumsum[:-2*n]) / float(n)
    return arr
#print(moving_average(a1))
for i in range(1,4):
    data = np.loadtxt(f'/Users/mikhail/Desktop/python_3sem/laba/lab3/epis2/signal0{i}.dat',dtype = float)
    fig, axes = plt.subplots(1,2)
    axes[0].plot(data, color = 'green') 
    axes[0].set_title('Сигнал до усреднения')
    axes[1].plot(running_mean(data))
    axes[1].set_title('Сигнал после усреднения')
    plt.show()
