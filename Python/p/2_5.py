def f(y, z):
    lst = []
    for i in range(len(z)):
        lst.append(abs(y[i] - z[i]))
    return max(lst)


print(f([1, 0.5, 1], [0.5, 2, 1]))
