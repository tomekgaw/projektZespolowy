import numpy as np
import functools
u = np.array([[2+5j, 5+3j], [1+2j, -2+8j]])
x = np.array( [[3+4j, -1+5j], [7+9j, 4+10j]])
print(np.dot(u,x))

def multiply(m,b):
    C = np.array([[1, 0, 1],
                  [0, 1, 1]])
    H = np.array([[b.real-b.imag, 0, 0],
                  [0, b[0].real+b.imag, 0],
                  [0, 0, b.imag]])
    D = np.array([[1, 0],
                  [0,1],
                  [1,-1]])
    x = np.array([m.real,m.imag])
    W = functools.reduce(np.dot, [C,H,D,x])
    re,im = W
    e = re+im*1j
    return e

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

m0 = multiply(d0,d[0])
m1 = multiply(d1,d[1])
m2 =  multiply(d2,d[2])
m3 =  multiply(d3,d[3])
m4 = multiply(d4,d[4])
m5 =  multiply(d5,d[5])
m6 =  multiply(d6,d[6])
print(d1,d[1])
# mnożenia
y[0,0] = m0 + m4
y[0,1] = m0 + m1 + m2 + m6
y[1,1] = m0 + m1 + m2 + m5
y[1,0] = m0 + m3 + m2 + m5
#
print(y)