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
# def translate(value: int, foundation: int = 2) -> int:
#     ret_value = ""
#     while value > 0:
#         ret_value += str(value % foundation)
#         value = value // foundation
#     return "".join(ret_value[:: -1])
#
#
# in_value = input().split()
# if len(in_value) == 2:
#     print(translate(int(in_value[0]), int(in_value[1])))
# else:
#     print(translate(int(in_value[0])))


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


# 2.8 Файлы
# https://stepik.org/lesson/305015/step/3?unit=287494

# with open(input(), "r", encoding='utf-8') as file:
#     print(file.read())


# my_sum = 0
# with open("f:/numbers.txt", "r", encoding='utf-8') as file:
#     for txt_num in file:
#             my_sum += int(txt_num.strip())
#
# print(my_sum)

# my_list = []
# with open("f:/Abracadabra.txt", "r", encoding='utf-8') as file:
#     for txt_num in file:
#         my_list.append(txt_num)
# print(my_list[-2])

#
# """
# "mean1.txt"
# 4
# "sheet1.txt"
# Аттила 2 (экзамен)
# Бонапарт Наполеон (неявка)
# Гассан Абдуррахман ибн Хоттаб 5 (автомат)
# Задойный Алексей Владимирович 5 (экзамен)
# Колонна-Валевский Александр Флориан Жозеф (недопуск)
# Цезарь Гай Юлий 4 (экзамен)
# """

# s = 0
# counter = 0
# with open("d:/sheet.txt", "r", encoding='utf-8') as file1:
#     for txt_num in file1:
#         t_list = txt_num.split()
#         if t_list[-1] in ["(экзамен)", "(автомат)"]:
#             s += int(t_list[-2])
#             counter += 1
# print(s, counter, s/counter)
#
# s2 = 0
# with open("d:/mean1.txt", "r", encoding='utf-8') as file1:
#     t = (list(map(float, file1)))
#
# print("OK" if s/counter == t[0] else "ERROR")


# import os.path
# # f_name = input()
# f_name = "d:/git"
# # Проверьте есть ли такой файл (и файл ли это) и если он есть - выведите содержимое. Иначе выведите одну из 2 ошибок.
# if os.path.exists(f_name):
#     if os.path.isfile(f_name):
#         with open(f_name, "r", encoding='utf-8') as file:
#             print(file.read())
#     else:
#         print("ERROR:")
#         print("Это каталог, а не файл")
# else:
#     print("ERROR:")
#     print("Файл не существует")


# in_str = input()
# with open('d:/output.txt', 'w', encoding='utf-8') as file:
#     file.write(in_str)


#  проверить есть файл его прочесть, там нечто вроде такого:
# https://stepik.org/lesson/305015/step/15?unit=287494
# event 4 - 'git fetch origin' -- это нужно добавить
# event 3 - 'git log -2'
# event 2 - 'git log'
# event 1 - 'git status'
#  если файл не существует, сохранить event с номером 1: "event 4 - 'git fetch origin'"
#  если существует, прочитать содержимое файла
# это нужно прочитать
# import os.path
# event = "git fetch origin" # input()
# file_name = "d:/git.log"  # input()
# event_number = 1
# lines = []
# if os.path.isfile(file_name):
#     # файл существует, читать...
#     with open(file_name, 'r', encoding='utf-8') as file:
#         lines = file.readlines()
#         # event_number = len(lines) + 1
#         for line in lines:
#             if line.startswith("event"):
#                 event_number += 1
# lines = [f"event {event_number} - '{event}'\n"] + lines
#
# with open(file_name, 'w', encoding='utf-8') as file:
#     file.writelines(lines)
#
#
# """
# event 3 - 'git log -2'
# event 2 - 'git log'
# event 1 - 'git status'
# """


