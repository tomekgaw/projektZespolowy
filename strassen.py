import numpy as np

u = np.array([[2, 5], [1, -2]])
x = np.array( [[3, -1], [7, 4]])

print(np.dot(u,x))
d = np.empty(7)
# wektor d z macierzy u
d[0] = u[0,0]
d[1] = u[1,0] + u[1,1]
d[2] = -u[0,0] + d[1]   # u[1,0]+u[1,1]
d[3] = u[1,1]
d[4] = u[0,1]
d[5] = u[0,0] - u[1,0]
d[6] = u[0,1] - d[2]

y = np.zeros([2,2])

# operacje prowadzące do mnozen z wektorem d[i]

d0 = x[0,0]
d1 = x[0,1]- d0
d4 = x[1,0]
d6 = x[1,1]
d2 = -d1 + d6
d3 = d4 - d2
d5 = d6 - x[0,1]

# d0 = x[0,0]
# d1 = x[0,1]- d0
# d2 = -d1 + x[1,1]
# d3 = x[1,0] -d2
# d4 = x[1,0]
# d5 = x[1,1] - x[0,1]
# d6 = x[1,1]

# mnożenia
y[0,0] = d0*d[0] + d4*d[4]
y[0,1] = d0*d[0] + d1*d[1] + d2*d[2] + d6*d[6]
y[1,1] = d0*d[0] + d1*d[1] + d2*d[2] + d5*d[5]
y[1,0] = d0*d[0] + d3*d[3] + d2*d[2] + d5*d[5]


print(y)