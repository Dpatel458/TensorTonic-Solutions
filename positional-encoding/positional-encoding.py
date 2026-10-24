import numpy as np

def positional_encoding(seq_len: int, d_model: int, base: float = 10000.0) -> np.ndarray:
    """
    Returns a NumPy array of shape (seq_len, d_model).
    """
    mat = [[0 for _ in range(d_model)]
              for _ in range(seq_len)]
    
    for i in range(seq_len):
        for j in range(d_model):
            exponent = (j // 2) * 2 / d_model
            denominator = base ** exponent
    
            if j % 2 == 0:
                mat[i][j] = np.sin(i / denominator)
            else:
                mat[i][j] = np.cos(i / denominator)

    return np.asarray(mat)
    pass