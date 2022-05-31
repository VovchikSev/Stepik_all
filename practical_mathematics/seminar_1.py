#  3.2 ДЗ семинара 1 Предел функции
# from math import atan
#
#
# def f(x):
#     return 2 * atan(x)
#
#
# x_ = 100000000
# lim = round(f(x_), 3)
#
# while True:
#     f_x = round(f(x_), 3)
#
#     if lim == f_x:
#         break
#     else:
#         lim = f_x
#         x_ += 1
# print(lim)

#  3.2 ДЗ семинара 2. Производная
from math import e
import numpy as np
import matplotlib.pyplot as plt


def f(x_p):
    return x_p ** 2
    # return e ** x_p


# def def_e(x_0, delta_x):
#     return (f(x_0 + delta_x) - f(x_0)) / delta_x


def g(x_p):
    return a * x_p + b


x0 = 3
dx = .0001
a = (f(x0 + dx) - f(x0)) / dx    # def_e(x0, dx)
b = f(x0) - a * x0
print(a)
print(b)
x = np.arange(-1, 2, .01)
plt.plot(x, f(x))
plt.plot(x, g(x))
plt.grid()
plt.show()


