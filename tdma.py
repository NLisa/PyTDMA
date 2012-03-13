import numpy as np
import _tdma

def tdma(A, b):
    """Tridiagonal matrix solve.
    
    Arguments:
    - `A`: Tridiagonal system of equations.
    - `b`: Right hand side of A * x = b.
    """
    lower = np.hstack((0, np.diag(A, -1)))
    middle = diag(A)
    upper = np.hstack((np.diag(A, 1)), 0)
    return _tdma.tdma(lower, middle, upper, b)
