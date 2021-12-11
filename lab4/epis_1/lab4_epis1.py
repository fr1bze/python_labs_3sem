import scipy as sc
import sympy as sp
n = 9 
matrix = sp.zeros(n, n)
ro, la, mu = sp.symbols('ro la mu')
ro = -1 / ro
matrix[0,3] = -(la + 2* mu)
matrix[0,6] = -la
matrix[0,8] = -la
for i in range(3): 
    matrix[3+i,i] = ro
for i in range(2):
    matrix[1+i, 4+i] = -mu
print(*matrix.eigenvals(),sep = '\n')

