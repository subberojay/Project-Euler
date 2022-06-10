
from math import log, ceil

def p(L, n):
    base = log(L, 2)
    step = log(L + 1, 2) - base
    m = 0
    while m < n:
        if ceil(base) - base < step:
            m += 1
        base += log(10, 2)
    return ceil(base - log(10, 2))





