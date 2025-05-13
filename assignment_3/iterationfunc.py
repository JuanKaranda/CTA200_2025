import numpy as np

def iteration(c, max_iter):
    """
    Determines the number of iterations it takes for the sequence z_{n+1} = z_n^2 + c to escape,
    or returns max_iter if it remains bounded.

    Parameters:
    c -------- Float-like, complex number
    max_iter - Integer-lik, maximum number of iterations

    Outputs:
    i -------- Integer-like, number of iterations until |z| > 2, or max_iter if bounded
    """
    z = 0
    for i in range(max_iter):
        z = z**2 + c
        if abs(z) > 2:
            return i
    return max_iter
