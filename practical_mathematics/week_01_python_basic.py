# first = int(input())
# second = int(input())

# """
# сумму чисел
# разность первого и второго
# разность второго и первого
# произведение
# частное от деления первого на второе
# остаток от деления второго на первое
# первое число, возведённое в степень второго
# """
# print(first + second)
# print(first - second)
# print(second - first)
# print(first * second)
# print(first / second)
# print(second / first)
# print(second % first)
# print(first ** second)

# first = int(input())
# second = int(input())
# print(int(first / second))

# a = float(input())
# b = float(input())
# c = float(input())
# p = a + b + c
# print(p)
# p = p / 2
# s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# print(s)

# Площадь ромба
# ac = float(input())
# bd = float(input())
# s = (ac * bd) / 2
# print(int(s))
# print(round(s, 1))
# print(s)

# Площадь шестиугольника и 5 треугольников
# a = float(input())
# s = ((3 ** 0.5) / 4) * a ** 2
# s = s * 11
# print(s)
# print(round(s))

# 9 друзей шестиугольника
# def s_trio(in_a: float) -> float:
#     return ((3 ** 0.5) / 4) * in_a ** 2
#
#
# a = float(input())
# s_f = 6 * s_trio(a) + 6 * s_trio(a / 2) + 3 * (a ** 2)
# print(round(s_f))
# print(s_f, round(s_f))

# Додекаэдр
# a = float(input())
# s = 3 * a ** 2 * (5 * (5 + 2 * 5 ** 0.5)) ** 0.5
# v = a ** 3 / 4 * (15 + 7 * (5 ** 0.5))
# print(round(s, 2))
# print(round(v, 2))

# про муху.
# L = float(input())
# v1 = float(input())
# v2 = float(input())
# vm = float(input())
#
# t = L / (v1 + v2)
# print(vm * t)


# my_list1 = list(map(int, input().split()))
# my_list2 = list(map(int, input().split()))
# print(f"{sum(my_list1)}#{sum(my_list2)}")

# наименьший делитель числа
# in_value = int(input())
# divider = 0
# stop_value = int(in_value ** .5)
# current_divider = 2
# count_iter = 1
# while current_divider <= stop_value:
#     print(count_iter)
#     if not in_value % current_divider:
#         divider = current_divider
#         break
#     current_divider += 1
#     count_iter += 1
# print(divider if divider else in_value)

# Считайте целое число n
# Напечатайте кубы всех натуральных чисел, меньших |n|, каждое с новой строки.
# [print(value ** 3) for value in range(1, abs(int(input())))]

# def dfactorial(n):
#     if n <= 0:
#         return 1
#     return n * dfactorial(n - 2)
#
# print(dfactorial(5))

# https://stepik.org/lesson/59468/step/10?unit=37347
# def convert(L: list) -> list:
#     return list(map(lambda value: value if type(value) == int else int(value), L))
#
#
# print(convert([1, 2, '3', '4', '5', 6]))

# https://stepik.org/lesson/59468/step/11?unit=37347
# def translate(value: int, foundation: int) -> int:
#     ret_value = ""
#     while value > 0:
#         ret_value += str(value % foundation)
#         value = value // foundation
#     print(*reversed(ret_value), sep="")
#
#
# translate(19, 2)

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# def sf(n):
#     mult = 1
#     for index in range(n + 1):
#         mult *= factorial(index)
#     return mult
#
#
# print(sf(2))


# def maxId(L: list) -> int:
#     max_value_index = 0
#     for index in range(len(L)):
#         if int(L[index]) > int(L[max_value_index]):
#             max_value_index = index
#     return max_value_index
#
#
# print(maxId([999]))
