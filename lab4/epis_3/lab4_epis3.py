from numpy.core.function_base import linspace
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
from scipy.integrate import odeint

#sympy
x=sp.symbols('x')
y=sp.symbols('y', cls=sp.Function)
a = sp.dsolve(sp.Eq(y(x).diff(x), (-2)*y(x)), ics={y(0): sp.sqrt(2)})
x_1 = np.arange(0, 10, 0.1)
y_1 = np.array([np.sqrt(2)*sp.exp(-2*x) for x in x_1])
print(a)

#scipy
def solve(y,x):
    return -2*y
y0 = sc.sqrt(2)
x_sc = np.arange(0,10,0.1)
y_sc = odeint(solve, y0, x_sc)
y_2 = y_sc.T
#print(y_sc)
y_ = y_1 - y_2
#построение графиков
fig, ax = plt.subplots(1,3)
ax2 = ax[0].plot(x_1,y_1) 
ax[0].set(title = 'Sympy solution')
ax1 = ax[1].plot(x_sc,y_2[0],color = 'green')
ax[1].set(title = 'Scipy solution')
ax3 = ax[2].plot(x_sc, y_[0])
ax[2].set(title = 'Difference')
plt.show()

