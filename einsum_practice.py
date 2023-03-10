import numpy as np



a = np.arange(100).reshape(10,10)
print(np.einsum('i...', a))


def trace(x):
    return np.einsum('ii')



