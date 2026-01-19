import numpy as np
v = np.arange(100)
print(v)
A = v.reshape(10, 10)
print(A)

A_T = A.T
print(A_T)

A_x2 = A*2
print(A_x2)

diag_A = np.diag(A)
print(diag_A)

I = np.eye(10)
print(I)

AxI = A @ I
print(AxI)