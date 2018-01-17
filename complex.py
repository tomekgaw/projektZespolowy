import numpy as np
import functools
u = np.array([[2+5j, 5+3j], [1+2j, -2+8j]])
x = np.array( [[3+4j, -1+5j], [7+9j, 4+10j]])
print(np.dot(u,x))
# m = np.array([[2+5j], [5+3j]])
#
# C = np.array([[1, 0, 1],
#               [0, 1, 1]])
# H = np.array([[m[1].real-m[1].imag, 0, 0],
#               [0, m[1].real+m[1].imag, 0],
#               [0, 0, m[1].imag]])
# D = np.array([[1, 0],
#               [0,1],
#               [1,-1]])
# x = np.array([[2],
#               [5]])
#
# W = functools.reduce(np.dot, [C,H,D,x])
# print(W)
d = np.empty((7,1),dtype=complex)
# wektor d z macierzy u
d[0] = u[0,0]
d[1] = u[1,0] + u[1,1]
d[2] = -u[0,0] + d[1]   # u[1,0]+u[1,1]
d[3] = u[1,1]
d[4] = u[0,1]
d[5] = u[0,0] - u[1,0]
d[6] = u[0,1] - d[2]
#
y = np.zeros([2,2],dtype=complex)
#
# # operacje prowadzące do mnozen z wektorem d[i]
#
d0 = x[0,0]
d1 = x[0,1]- d0
d4 = x[1,0]
d6 = x[1,1]
d2 = -d1 + d6
d3 = d4 - d2
d5 = d6 - x[0,1]

# mnożenia
y[0,0] = d0*d[0] + d4*d[4]
y[0,1] = d0*d[0] + d1*d[1] + d2*d[2] + d6*d[6]
y[1,1] = d0*d[0] + d1*d[1] + d2*d[2] + d5*d[5]
y[1,0] = d0*d[0] + d3*d[3] + d2*d[2] + d5*d[5]
#
print(y[0,0])