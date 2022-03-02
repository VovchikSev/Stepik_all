

# число трибоначи :)
# n = int(input())
# f1, f2, f3 = 1, 1, 1
# for i in range(n):
#     print(f1, end=' ')
#     f1, f2, f3 = f2, f3, f1 + f2 + f3

# получить количество и список студентов,
# вывести всех студентов и после пустой строки, только тех у которых 4 или 5
#  пример ввода
# 5
# Круглов 4
# Кузнецов 5
# Федин 4
# Тарасов 2
# Словецкий 3
# Вывод:
# Круглов 4
# Кузнецов 5
# Федин 4
# Тарасов 2
# Словецкий 3
#
# Круглов 4
# Кузнецов 5
# Федин 4
# мое решение
# students_count = int(input())
# full_list = []
# my_list = []
# for str_value in range(students_count):
#     full_list.append(input().split())
#     if int(full_list[len(full_list) - 1][1]) > 3:
#         my_list.append(full_list[len(full_list) - 1])
#
# for str_value in full_list:
#     print(*str_value)
# print()
# for str_value in my_list:
#     print(*str_value)
# красивое решение
# s = [input().split() for _ in range(int(input()))]
# for i in s:
#     print(*i)
# print()
# for i in s:
#     if int(i[1]) > 3:
#         print(*i)

#  еще вариант, без преобразования в целое
# students = [tuple(input().split()) for _ in range(int(input()))]
#
# for student in students:
#     print(*student)
#
# print()
#
# for name, grade in students:
#     if grade in '45':
#         print(name, grade)


# Дополните приведенный код так, чтобы он вывел список, содержащий средние арифметические значения
# чисел каждого вложенного кортежа в заданном кортеже кортежей numbers.

# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
#
# print([sum(i) / len(i) for i in numbers])


# Дополните приведенный код так, чтобы переменная new_tuples, содержала список кортежей на основе списка tuples
# с последним элементом каждого кортежа, замененным на численное значение 100100.
# моё решение.
# tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
# new_tuples = []
#
# # my_list = list(tuples)
# # print(type(my_list[1]))
#
# for i in tuples:
#
#     i_list = list(i[:-1])
#     i_list.append(100)
#     new_tuples.append(tuple(i_list))
#     # print(i_list)
# print(new_tuples)


# нормальное решение.
# tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
# new_tuples = [i[:-1] + (100,) for i in tuples]
# print(new_tuples)


# tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
# my_list = list(tuples)
# non_empty_tuples = []
# for i in my_list:
#     print(i, len(i))
#     if i:
#         non_empty_tuples.append(i)
#
# print(non_empty_tuples)
