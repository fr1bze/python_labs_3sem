import numpy as np
from numpy import ma, mat
from numpy.core.fromnumeric import shape
from scipy import linalg
import matplotlib.pyplot as plt

path = "/Users/mikhail/Desktop/python_3sem/laba/lab4/epis_2/small.txt"
matrix = np.loadtxt(path, skiprows = 1, dtype = np.float64)
n = np.min(shape(matrix)) #n - размерность, поэтому выбираем по сути сколько компонент у вектора (длина строки)
#print(matrix[:n])
#print(matrix[n:])
x = linalg.solve(matrix[:n],matrix[n:].T)
#print(x)
plt.bar(np.arange(n), height= list(x.T[0]))
plt.grid('on')
plt.show()