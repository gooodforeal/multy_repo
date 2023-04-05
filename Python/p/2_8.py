import matplotlib.pyplot as matplotlib
import math as m


def f1(y, z):
    d = 0
    for i in range(len(y)):
        d += (y[i] - z[i]) ** 2
    return m.sqrt(d)


def f2(y, z):
    x = 0
    for i in range(len(y)):
        x += abs(y[i] - z[i])
    return x


def f3(y, z):
    res = []
    for i in range(min([len(y), len(z)])):
        res.append(abs(y[i]-z[i]))
    return max(res)


def f4(y, z):
    d = 0
    for i in range(len(y)):
        d += (y[i] - z[i]) ** 2
    return d


def f5(y, z, h = 5):
    x = 0
    for i in range(len(y)):
        x += abs(y[i] - z[i])**h
    return x**(1/h)


def visualize(distance_metrics, y, z, move=1):
    moved_z = [i + move for i in z]
    distance_differences = []
    for distance in distance_metrics:
        distance_before_move = distance(y, z)
        distance_after_move = distance(y, moved_z)
        distance_difference = distance_after_move - distance_before_move
        distance_differences.append(distance_difference)
    x = range(0, len(distance_differences))
    figure, axis = matplotlib.subplots()
    axis.bar(x, distance_differences)
    axis.set_xticks(x, labels=[f'd_{i + 1}' for i in x])


mas = [f1, f2, f3, f4, f5]
visualize(mas, [1, 0.5, 1], [0.5, 2, 1], 0.5)
visualize(mas, [1, 0.5, 1], [0.5, 2, 1], 1)
visualize(mas, [1, 0.5, 1], [0.5, 2, 1], 1.5)
matplotlib.show()
