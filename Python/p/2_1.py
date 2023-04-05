import math


def f(n, m):
    res = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            res += (math.ceil(i) - 76 * j)
    res *= 22
    a = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            a += (42 * j + (90 * j ** 4) - 8)
    a /= 31
    res -= a
    return res


print(f(21, 83))
