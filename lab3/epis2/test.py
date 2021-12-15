import numpy as np 
a = np.linspace(1, 100, 100)
x = np.cumsum(a[-5:]) / 5
y = x.shape[0]
print(type(y))