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

def orth2(vs, v = [], tol = 1e-2) -> np.ndarray: #Note this function will always return a numpy array
    """
        v: np.ndarray of shape 1xn or 0xn with n being the number of dimensions (optional)
        vs: np.ndarray of shape Nxn with N being the number of vectors and n being the number of dimensions
        if v is not provided, we compare every combination of vectors in vs

        Simplified -> vs is a vector of vectors(matrix) and v is a single vector.
        """
    if type(vs) != np.ndarray:
        vs = np.array(vs)
    vs = vs/np.linalg.norm(vs, axis = 1, keepdims = True)#Normalize the vectors
    if len(v) == 0:
        return (np.abs(np.dot(vs, vs.T))<(1-tol)).astype(int)
    if type(v) != np.ndarray:
        v = np.array(v)
    if len(v.shape)>1:
        v = v.flatten();
    v = v/np.linalg.norm(v)#Normalize the vector
    return (np.abs(np.dot(v, vs.T))<(1-tol)).astype(int)

if __name__ == "__main__":
    # Check if both functions have the same output and that the outputs match the second function with an extra argument
    vectors = np.eye(3);
    v = np.array([1, 0, 0])
    a = orthonormal(vectors)
    b = orth2(vectors)
    c = orth2(vectors, v)
    print(a)
    print(b)
    print(c)