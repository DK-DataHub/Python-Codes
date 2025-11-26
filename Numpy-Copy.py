import numpy as np
a = np.array([1, 2, 3, 4, 5])
x = a.copy()
a[2] = 77
print(x)
print(a)
