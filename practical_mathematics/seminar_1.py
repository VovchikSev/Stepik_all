#  3.2 ДЗ семинара 1 Предел функции
from math import atan


def f(x):
    return 2 * atan(x)


x_ = 100000000
lim = round(f(x_), 3)

while True:
    f_x = round(f(x_), 3)

    if lim == f_x:
        break
    else:
        lim = f_x
        x_ += 1
print(lim)
