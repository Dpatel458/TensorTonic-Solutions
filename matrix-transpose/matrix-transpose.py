import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    b = np.asarray(A)
    z = [ [0 for _ in range(len(b))]
            for _ in range(len(b[0]))]

    for i in range(len(b)):
        for j in range(len(b[0])):
            z[j][i] = b[i][j]

    return np.asarray(z)
    pass
