from matscaling import *
import numpy as np

A = np.array([[1, 2], [0, 1]], dtype=float)
r = np.array([1, 1], dtype=float)
c = np.array([1, 1], dtype=float)

print("init state")
print(A)
print("----------------")

for i in range(100):
    print("scale row")
    A = matscaling_Arow_once(A, r)
    print(A)
    print("----------------")

    print("scale col")
    A = matscaling_Acol_once(A, c)
    print(A)
    print("----------------")
