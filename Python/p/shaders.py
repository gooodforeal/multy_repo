import math
import tkinter as tk


def pyshader(func, w, h):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [max(min(int(c * 255), 255), 1)
                            for c in func(x / w, y / h)]
    return bytes('P6\n%d %d\n255\n' % (w, h), 'ascii') + scr


def func(x, y):
    y_ = y * 2 - 1
    body = -((x - 0.5)**2 + (y - 0.5)**2 - 0.1)
    eye = -((x - 0.6)**2 + (y - 0.3)**2 - 0.003)
    mouth = (0.5 - abs(y_ * 0.85) + x - 1)
    res = mouth * eye
    res = (-abs(res-body)+res+body)/2
    res *= 1e6
    return res, res, 0


label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()


def pyshader(func, w, h):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [max(min(int(c * 255), 255), 0)
            for c in func(x / w, y / h)]
    return bytes('P6\n%d %d\n255\n' % (w, h), 'ascii') + scr


def func(x, y):
    res = -((x - 0.5)**2 + (y - 0.5)**2 - 0.1) * 10
    res1 = -((x - 0.55)**2 + (y - 0.55)**2 - 0.1) * 10
    return res, res1, 0


label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()
