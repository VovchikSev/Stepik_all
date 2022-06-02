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
# from math import e
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# def f(x_p):
#     return x_p ** 2
#     # return e ** x_p
#
#
# # def def_e(x_0, delta_x):
# #     return (f(x_0 + delta_x) - f(x_0)) / delta_x
#
#
# def g(x_p):
#     return a * x_p + b
#
#
# x0 = 3
# dx = .0001
# a = (f(x0 + dx) - f(x0)) / dx    # def_e(x0, dx)
# b = f(x0) - a * x0
# print(a)
# print(b)
# x = np.arange(-1, 2, .01)
# plt.plot(x, f(x))
# plt.plot(x, g(x))
# plt.grid()
# plt.show()

#  3.2 ДЗ семинара 3. Список - чётные индексы
#
# n = int(input()) # Input and convert to int
# res = 0
# for value in range(n + 1):
#     # делятся на 5, но не делятся на 3
#     if not value % 5 and value % 3:
#         print(value % 3, value % 5, value)
#         res += value
# print(res)

list_a = [0, 2, 3, 4, 5, 19, 42]
list_b = [0, 6, 19, 33, 42, 55, 66, 77, 99, 101, 256]


# def common(list_a, list_b):
#     return list(set(list_a) & (set(list_b)))
#
# print(common(list_a, list_b))

# 8. front_x (с пустыми строками)
# Напишите функцию front_x(words), которая на вход принимает список строк и возвращает отсортированный по правилам:
# слова, начинающиеся с символа "x", идут первыми
# в лексикографическом порядке.


# def front_x(words):
#     # x_list =
#     # other_list = list(filter(lambda word: not str(word).startswith("x"), sorted(words)))
#     return list(filter(lambda word: str(word).startswith("x"), sorted(words))) + \
#            list(filter(lambda word: not str(word).startswith("x"), sorted(words)))
#     # лучше так return sorted(words, key=lambda x: (x[:1] != 'x', x))
#     # в сортировку передавать два параметра в tuple x: (x[:1] != 'x', x)  для sorted key=lambda
#     # сортировка идет в начале по первому ключу и далее по нисходящей.
#
#
# print(front_x(['x-files', 'xapple', 'xyz', '', 'apple', 'extra', 'mix']))

# 9. Числа Фибоначчи
# Напишите функцию fib(n), возвращающую n-е число Фибоначчи.
# def fib(n):
#     sqrt_5 = 5 ** .5
#     # максимальное значение n = 604 иначе размера инт не хватает
#     return int(((1 + sqrt_5) ** n - (1 - sqrt_5) ** n) / (2 ** n * sqrt_5))
#
# print(fib(604))

# 10. Простые числа
# def is_prime(n):
#     result = True
#     for value in range(2, int(n ** .5) + 1):
#         result = bool(n % value)
#         if not result:
#             break
#     return result
#
#
# print(is_prime(103))

#
s = input()
def fix_start(s):
    result = ''
    for index in range(len(s)):
        if index and s[index] == s[0]:
            result += '*'
        else:
            result += s[index]
    return result


print(fix_start(s))
