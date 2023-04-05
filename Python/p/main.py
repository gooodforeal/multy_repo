import math


def task31(x):
    x += x
    x += x
    y = x
    x += x
    x += y
    return x


def task32(x):
    x += x
    x += x
    x += x
    x += x
    return x


def task33(x):
    y = x
    x += x
    x += x
    x += x
    x -= -x
    x -= y
    return x


def task34():
    b, n, a = 2, 2, 6
    first_sum = sum(sum((34*j + 41)**4 - 93 * (c + 79 + c**3)**5 for c in range(1, b + 1)) for j in range(1, n + 1))
    second_mult = 1
    for k in range(1, a + 1):
        second_mult *= sum(22 * (c - 8)**5 - k**4 for c in range(1, b + 1))
    return first_sum - second_mult


def task35(x):
    if x < 13:
        return x**5
    elif 13 <= x < 87:
        return x**7 - 1 - (int(x)**3) / 54
    else:
        return (int(x)+1)**3


def task36(n):
    if n == 0:
        return 3
    else:
        return math.sin(task36(n - 1)) - 1 / 16 * task36(n - 1)**3


def fast_mul(a, b):
    s = 0
    while a >= 1:
        if a % 2 == 1:
            s += b
        a //= 2
        b *= 2
    return s


def fast_exp(b, e):
    s = b
    res = b
    while e > 1:
        res = fast_mul(res, s)
        e -= 1
    return res


print(fast_exp(2, 10))


try:
    assert fast_mul(10, 15) == 150
    assert fast_mul(12, 4) == 48
    assert fast_mul(9, 20) == 180
    assert fast_mul(5, 1) == 5
    print("[+] PASSED")
except AssertionError:
    print("[!] ERROR!")


def s2(y):
    if y < 128:
        return math.exp(y)**6
    elif 128 <= y < 143:
        return (int(y + y**2) + 1)**7 + 1 + (y**3 - 1)**2
    elif 143 <= y < 189:
        return y**6
    elif 189 <= y < 209:
        y**6 + (y / 83 - 0.02 - y**3)**3 + y**4
    else:
        return (55*y**2)**6 + ((y**2 - 39*y**3)**2) / 25


def s3(a, b, m):
    res = 0
    for j in range(1, m + 1):
        k = 1
        for c in range(1, b + 1):
            f = 0
            for i in range(1, a + 1):
                f += i**6 + (j/83 - 0.02 - i**3)**3 + c**4
            k *= f
        res += k
    return res


def s4(n):
    if n == 0:
        return 0.90
    elif n == 1:
        return -0.82
    else:
        return s4(n - 2) + (s4(n - 1)**2) / 16


def main(x, z, y):
    def f(a, b, c):
        return 91 * math.exp(a**2 - b - 54*c**3)**7
    n = len(z) - 1
    res = 0
    for i in range(1, n + 1):
        res += f(z[i//3], y[i//2], x[n + 1 - i])
    res *= 68
    res = "{:.2e}".format(res)
    return res


from tkinter import *
from tkinter import ttk


def square():
    window = Tk()
    canvas = Canvas(window, width=600, height=600)
    canvas.create_rectangle(100, 100, 500, 500, fill="black")
    canvas.pack()
    window.mainloop()


def circle():
    window = Tk()
    canvas = Canvas(window, width=600, height=600)
    canvas.create_oval([400, 400], [150, 150], fill="orange", outline=False)
    canvas.pack()
    window.mainloop()


def packman():
    window = Tk()
    canvas = Canvas(window, width=600, height=600)
    canvas.create_oval(400, 400, 150, 150, fill="yellow", outline="yellow")
    canvas.create_oval(450, 430, 20, 20, fill="black", outline="black")
    canvas.pack()
    window.mainloop()


square()
