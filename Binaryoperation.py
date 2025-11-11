import numpy as np
a = np.array([[1, 2, 3],
       [3, 4, 5],
       [4, 3, 2]])
b = np.array([[1, 2, 2],
       [3, 2, 2],
       [2, 4, 3]])
c = np.array([[2, 6, 8],
       [5, 4, 7],
       [3, 1, 0]])
#Binary operation
print("\nSum of all Array elements:\n", np.sum(a+b+c))
