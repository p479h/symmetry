import numpy as np

def orthonormal(vectors, tol = 1e-4):
    if len(vectors) == 0:
        print("input is empty")
    elif len(vectors) == 2:
        if np.dot(vectors[1], vectors[0]) == 0:
            orth = True
        else:
            orth = False
        return orth
    else:
        vectors = np.stack(vectors)
        orth = np.dot(vectors,vectors.transpose())
        orth[abs(orth) > 1] = 1
        orth[abs(orth) < tol] = 0
        orth = 1 - orth
        return orth
