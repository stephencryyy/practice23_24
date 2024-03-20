import numpy as np

def solve(A, b):
   return np.linalg.solve(A, b)

A = np.array([[-6, -5, -3, -8],
              [5, -1, -5, -4],
              [-6, 0, 5, 5],
              [-7, -2, 8, 5]], dtype=float)

b = np.array([101, 51, -53, -63], dtype=float)
x = solve(A, b)
print(x)