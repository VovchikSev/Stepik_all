# пример из теории
from math import sin, pi


def df_decorator(dx=0.01):
    def func_decorator(func):
        def wraper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res
        
        return wraper
    
    return func_decorator


@df_decorator(dx=0.00000001)
def sin_dx(x):
    return sin(x)


df = sin_dx(pi / 3)
print(df)

# Подвиг 1. Вводится строка целых чисел через пробел. Напишите функцию, которая преобразовывает эту строку в
# список чисел и возвращает их сумму. Определите декоратор для этой функции, который имеет один параметр start -
# начальное значение суммы.
# Примените декоратор со значением start=5 к функции и вызовите декорированную функцию
# для введенной строки s: s = input()
# Результат отобразите на экране.
