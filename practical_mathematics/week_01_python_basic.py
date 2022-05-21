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

my_list = input().split()
[print(value) for value in my_list if not value.startswith("*")]