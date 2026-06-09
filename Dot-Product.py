#Dot Product using numpy shortcut

import numpy as np

q = np.array([1,2,3,4,5])
k = np.array([1,2,3,4,5])

#Two standard ways to do the dot product
sol = np.dot(q,k)
sol2  = q@k
print(sol)
print(sol2)