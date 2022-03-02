# """
# На вход программе подается натуральное число nn. Напишите программу, которая создает матрицу
# размером n×n и заполняет её по следующему правилу:
# на главной диагонали на месте каждого элемента должно стоять число 0;
# на двух диагоналях, прилегающих к главной, число 1;
# на следующих двух диагоналях число 2, и т.д.
# """
# my_range = int(input())
# my_matrix = []
#
# for row_index in range(my_range):
#     my_matrix.append([])
#     for column_index in range(my_range):
#         my_matrix[row_index].append(abs(column_index - row_index))
#
# [print(*row) for row in my_matrix]

# """
# Отобразить на доске ходы ферзя
# немного помогу с формулой.
# если х1-х2 = у1-у2 ход по диагонали,
# или х1 = х2 или у1 = у2 ход по горизонтали и вертикали.
# ну и не забываем про абсолютное число. будет вам счастье в "пару" строк)))
# """
# liter, number = input()
# column_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
# row_dict = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
# RANGE = 8 # размер доски
# my_matrix = []
# x, y = column_dict[liter], row_dict[number]
# print(x, y)
# for row_index in range(RANGE):
#     my_matrix.append([])
#     for column_index in range(RANGE):
#         if row_index == row_dict[number] and column_index == column_dict[liter]:
#             my_matrix[row_index].append("Q")
#         elif abs(x - column_index) == abs(y - row_index) or (x == column_index or row_index == y):
#             my_matrix[row_index].append("*")
#         else:
#             my_matrix[row_index].append(".")
#
# for row_index in range(RANGE):
#     print(*my_matrix[row_index])

# """
# Латинским квадратом порядка nn называется квадратная матрица размером n×n,
# каждая строка и каждый столбец которой содержат все числа от 1 до n.
# Напишите программу, которая проверяет, является ли заданная квадратная матрица латинским квадратом.
# """
#
#
# my_range = int(input())
# my_matrix = [[int(i) for i in input().split()] for _ in range(my_range)]
# my_flag = True
#
# new_matrix = []
# for row in my_matrix:
#     new_matrix.append(row[::])
#
# for row in range(my_range):
#     my_index = len(my_matrix) + row
#     # print(row, my_index)
#     new_matrix.append([])
#     for column in range (my_range):
#         new_matrix[my_index].append(my_matrix[column][row])
#
# for row in new_matrix:
#     row.sort()
#     for column in range(my_range):
#         if column + 1 != row[column]:
#             my_flag = False
#             break
#     if not my_flag:
#         break
#
# print("YES" if my_flag else "NO")

# """
# Проверка на симметричность матрицы по побочной диагонали
# """
# def transpose(matrix):
#     res = []
#     rows = len(matrix)
#     column = len(matrix[0])
#     for column_index in range(column):
#         tmp = []
#         for row_Index in range(rows):
#             tmp = tmp + [matrix[row_Index][column_index]]
#         res = res + [tmp]
#     return res
#
#
# my_range = int(input())
# my_matrix = [[int(i) for i in input().split()] for _ in range(my_range)]
#
# new_matrix = []
#
# for row in my_matrix:
#     new_matrix.append(row[::-1])
# print("YES" if transpose(new_matrix) == new_matrix else "NO")


# """
# На вход программе подается нечетное натуральное число nn. Напишите программу, которая создает матрицу размером
# n×n заполнив её символами . . Затем заполните символами * среднюю строку и столбец матрицы,
# главную и побочную диагональ матрицы.
# Выведите полученную матрицу на экран, разделяя элементы пробелами.
# Sample Input 1:
# 5
# Sample Output 1:
# * . * . *
# . * * * .
# * * * * *
# . * * * .
# * . * . *
# """
# my_range = int(input())
# my_matrix = [[". " for _ in range(my_range)] for _ in range(my_range)]
# for row_index in range(my_range):
#     for column_index in range(my_range):
#         if column_index == row_index \
#                 or my_range == row_index + column_index + 1 \
#                 or column_index == my_range // 2 \
#                 or row_index == my_range // 2:
#             my_matrix[row_index][column_index] = "* "
#
#
# [print(*row) for row in my_matrix]
# """
# Напишите программу, которая транспонирует квадратную матрицу.
# строки становятся стобцами
# Sample Input 1:
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# Sample Output 1:
# 1 4 7
# 2 5 8
# 3 6 9
# """
#
# def transpose(matrix):
#     res = []
#     rows = len(matrix)
#     column = len(matrix[0])
#     for column_index in range(column):
#         tmp = []
#         for row_Index in range(rows):
#             tmp = tmp + [matrix[row_Index][column_index]]
#         res = res + [tmp]
#     return res
#
#
# my_range = int(input())
# my_matrix = [[int(i) for i in input().split()] for _ in range(my_range)]
# [print(*row) for row in transpose(my_matrix)]


# """
# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.
# (ниже побочной диагонали)
# 3
# 1 4 5
# 6 7 8
# 1 1 6
# """
#
# my_range = int(input())
# my_matrix = [[int(i) for i in input().split()] for _ in range(my_range)]
# d_index = - 1
# max_element = my_matrix[0][d_index]
#
# # for row in my_matrix:
# #     # print(row[d_index::])
# #     # print(max(row[d_index::]))
# #     if max_element < max(row[d_index::]):
# #         max_element = max(row[d_index::])
# #     d_index -= 1
#
# [print(*row) for row in my_matrix]

# """
# На вход программе подается строка текста, содержащая символы и число nn. Из данной строки формируется список.
# Напишите программу, которая разделяет список на вложенные подсписки так, что nn последовательных элементов принадлежат
# разным подспискам.
# Sample Input 1:
# a b c d e f g h i j k l m n
# 3
# Sample Output 1:
# [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
# """
# matrix_a = [i for i in input().split()]
# my_len = int(input())
# matrix_b = []
# b_count = 0
# while b_count < my_len:
#     print(matrix_a[b_count::my_len])
#     matrix_b.append(matrix_a[b_count::my_len])
#     b_count += 1
#
# print(matrix_b)
