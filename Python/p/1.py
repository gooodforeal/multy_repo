import math


def main(x, z, y):
    n = len(z)
    res = 0
    for i in range(1, n + 1):
        a = z[math.ceil(i / 3 - 1)]
        b = y[math.ceil(i / 2 - 1)]
        c = x[n - i]
        res += 91 * math.exp(a**2 - b - 54*c**3)**7
    res *= 68
    return res


print(main([-0.61, 0.61, -0.63, -0.96, 0.56, 0.06, 0.51], [0.04, -0.24, -0.16, 0.76, 0.29, -0.7, 0.33], [-0.35, -0.03, -0.37, -0.5, 0.06, 0.03, -0.72]))


