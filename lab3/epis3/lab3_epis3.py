import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
steps = 255
data = np.loadtxt('/Users/mikhail/Desktop/python_3sem/laba/lab3/epis3/start.dat')
#print(data)
A = np.eye(len(data), len(data)) #квадратная матрица с размерами n*n, 
                                       #где n - длина массива data 
A[0, len(data) - 1] = -1
for i in range(0, A.shape[0]):
    A[i][i-1] = -1
data_plt = [data]
for i in range(1, steps): 
    data_plt.append(data_plt[i-1] - 0.5 * A @ data_plt[i-1])
fig, ax = plt.subplots()
line, = ax.plot(data_plt[0])
ax.grid("on")
ax.set_xlim(left=-1, right=50)
ax.set_ylim(bottom=0, top=8)
ax.set_title(r"$\vec{u(x)}^{n+1}=\vec{u(x)}^{n}-0.5\cdot A\cdot\vec{u(x)}^{n}$")
def animate(i):
    line.set_ydata(data_plt[i])
    return line
#анимация и ее сохранение 
animation_ = animation.FuncAnimation(fig, animate, frames=steps, interval=80)
animation_.save("duwii.gif")