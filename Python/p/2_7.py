import math


def f(y, z):
    h = 5
    n = len(y)
    d = 0
    for i in range(n):
        d += abs(y[i] - z[i])**h
    d = d**(1/h)
    return d


print(f([1, 0.5, 1], [0.5, 2, 1]))
