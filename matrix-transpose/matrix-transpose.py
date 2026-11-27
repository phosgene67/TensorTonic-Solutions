import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    n = len(A) 
    m= len (A[0])
    out = np.empty((m,n),dtype = np.float64)
    for i in range(n):
        for j in range(m):
            out[j,i]=A[i][j]
    return out 
    pass
