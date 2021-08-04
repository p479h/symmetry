import numpy as np
import sys

from functions.math.orthonormal import orthonormal
from functions.math.orthonormal import orth2

v1 = np.array([1,2,3])
v2 = np.array([0,0,1])

print(orthonormal([v1,v2]))

v2 = np.array([0,0,2])

print(orthonormal([v1,v2]))

v3 = np.array([0,0,-1])

vectors = np.stack([v1,v2,v3])
print(vectors)

print(len([v1,v2,v3]))

print(orthonormal([v1,v2,v3]))


k = np.array([0,0,1], dtype = float)
k /= np.linalg.norm(k)
x = np.random.randn(3)
x -= x.dot(k) * k
x /= np.linalg.norm(x)

y = np.cross(k,x)

print(k,x,y)

print(orthonormal([k,x,y]))

print(orth2([k,x,y,v1]))

v1 = np.array([0, 0 , 1])
v2 = np.array([0, 0 , 2])
v3 = np.array([0, 1 , 0])

print(orth2([v1,v2,v3]))

