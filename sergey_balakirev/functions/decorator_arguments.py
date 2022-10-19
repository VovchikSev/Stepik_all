# пример из теории
# from math import sin, pi
#
#
# def df_decorator(dx=0.01):
#     def func_decorator(func):
#         def wrapper(x, *args, **kwargs):
#             res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
#             return res
#
#         return wraper
#
#     return func_decorator
#
#
# @df_decorator(dx=0.00000001)
# def sin_dx(x):
#     return sin(x)
#
#
# df = sin_dx(pi / 3)
# print(df)

# Подвиг 1. Вводится строка целых чисел через пробел. Напишите функцию, которая преобразовывает эту строку в
# список чисел и возвращает их сумму. Определите декоратор для этой функции, который имеет один параметр start -
# начальное значение суммы.
# Примените декоратор со значением start=5 к функции и вызовите декорированную функцию
# для введенной строки s: s = input()
# Результат отобразите на экране.

# def pre_decorator(start):
#     def decorator(function):
#         def wrapper(message):
#             return function(message) + start
#         return wrapper
#     return decorator
#
#
# @pre_decorator(start=5)
# def modificate(text):
#     text = [int(i) for i in text.split()]
#     return sum(text)
#
#
# s = input()
# result = modificate(s)
# print(result)

"""
Подвиг 2. Объявите функцию, которая возвращает переданную ей строку в нижнем регистре (с малыми буквами).
Определите декоратор для этой функции, который имеет один параметр tag, определяющий строку с названием тега и начальным
значением "h1". Этот декоратор должен заключать возвращенную функцией строку в теге tag и возвращать результат.
Пример заключения строки "python" в тег h1: <h1>python</h1>
Примените декоратор со значением tag="div" к функции и вызовите декорированную функцию для введенной строки s:
s = input()
Результат отобразите на экране.
Sample Input: Декораторы - это классно! -> <div>декораторы - это классно!</div>
"""


def pre_decorator(tag: str = "h1"):
    def in_decorator(func):
        def wrapper(message: str) -> str:
            return f"<{tag}>{func(message)}</{tag}>"
        return wrapper

    return in_decorator


@pre_decorator(tag="div")
def prepare_str(s: str) -> str:
    return s.lower()

print(prepare_str(input()))