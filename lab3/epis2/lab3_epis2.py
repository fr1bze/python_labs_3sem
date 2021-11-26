import numpy as np
import matplotlib.pyplot as plt
path1 = '/Users/mikhail/Desktop/python_3sem/laba/lab3/epis2/signal01.dat'
path2 = '/Users/mikhail/Desktop/python_3sem/laba/lab3/epis2/signal02.dat'
path3 = '/Users/mikhail/Desktop/python_3sem/laba/lab3/epis2/signal03.dat'
a1 = np.loadtxt(path1)
a2 = np.loadtxt(path2)
a3 = np.loadtxt(path3)
def moving_average(a, n = 10):
    res = np.cumsum(a, dtype=float)
    res[n:] = res[n:] - res[:-n]
    return res[n - 1:] / n
#print(moving_average(a1))
print(np.shape(a1),np.shape(moving_average(a1)))
plt.plot(a1)
plt.plot(moving_average(a1))
plt.show()