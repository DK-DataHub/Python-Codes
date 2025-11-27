import numpy as np
x = np.array([[[1, 2, 3],[4, 5, 6]],[[7, 8, 9],[10, 11, 12]]])
for y in x:
  for z in y:
    for x in z:
      print(x)
