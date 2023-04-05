import math


def f(y, z):
    n = len(y)
    d = 0
    for i in range(n):
        d += (y[i] - z[i])**2
    d = math.sqrt(d)
    return d


print(f([1, 0.5, 1], [0.5, 2, 1]))
