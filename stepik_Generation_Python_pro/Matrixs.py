# """
# входное:
# 3 2
# 2 5
# 6 7
# 1 8
#
# 2 3
# 1 2 1
# 0 1 0
# """
#
# # def rotate_matrix_left(matrix):  # Это все не нужно, работать напрямую
# #     rows, column = len(matrix), len(matrix[0])
# #     matrix_result = [[None] * rows for _ in range(column)]
# #
# #     for row_index in range(len(matrix_result)):
# #         for column_index in range(len(matrix_result[0])):
# #             matrix_result [row_index][column_index] = matrix[column_index][row_index]
# #     # for row_m in matrix_result:
# #     #     print(*row_m)
# #     return matrix_result
#
# def print_matrix(matrix):
#     for arr in matrix:
#         print(*arr)
#
#
# rows_m1, column_m1 = [int(i) for i in input().split()] # количество строк колонок в матрицах
# matrix_m1 = [[int(i) for i in input().split()] for _ in range(rows_m1)]
# input()
# rows_m2, column_m2 = [int(i) for i in input().split()] # количество строк колонок в матрицах
# matrix_m2 = [[int(i) for i in input().split()] for _ in range(rows_m2)]
# # количество столбцов в первой матрице совпадает с количеством строк во второй матрице
# # создание результирующей матрицы: строк как с первой столбцов как во второй
#
# matrix_res = [[0] * column_m2 for _ in range(rows_m1)]
# """
#  column_m1 = rows_m2 ==  column_m3
#  нас есть 3 матрицы:
#  A(n*m),
#  B(m*k)
#  и их произведение
#  C(n*k).
#                  n       m
#  A = matrix_m1 rows_m1*column_m1
#                     m     k
#  B = matrix_m2  rows_m2*column_m2 (m = rows_m2 = rows_m2)
#
#  C =  matrix_res n * k
#  Соответственно нам нужно заполнить матрицу n*k.
#  Для этого используем два цикла как и для любой другой матрицы.
#  Но поскольку каждый элемент матрицы С - это сумма произведений элементов строк на элементы столбцов(),
#  нам понадобится еще один цикл. В результате нам нужно использовать 3 цикла (от 0 до n, от 0 до k, от 0 до m).
#  c[ i ][ j ] += a[ i ][ k ] * b[ k ][ j ]
# Сколько строк нам нужно в результирующей матрице? - n, следовательно, внешний цикл нужно выполнить range(n) раз.
# Сколько элементов нужно в каждой строке? - k, следовательно, второй цикл нужно выполнить range(k) раз.
# Сколько шагов суммирования для каждого элемента? - m, следовательно, третий цикл выполнить range(m) раз.
# Имея этот каркас, додумал тело третьего цикла.
# """
# for i_index in range (rows_m1):
#     for j_index in range(column_m2):
#         for k_index in range(rows_m2):
#             matrix_res[i_index][j_index] += matrix_m1[i_index][k_index] * matrix_m2[k_index][j_index]
# # for row_index in range(rows_m1): # По строкам умножаемого
# #     for column_index in range(column_m1): #
# #         for k_index in range(column_m2):
# #             matrix_res[row_index][column_index] += matrix_m1[row_index][k_index] * matrix_m2[k_index][column_index]
#             # оригинал c[ i ][ j ] += a[ i ][ k ] * b[ k ][ j ] где к количество столбцов
#             # res[ row_m1 ][ column_m1 ] += m1[ row_m1 ][ rows_m2 ] * m2[ rows_m2 ][ column_m1 ]
#
# print_matrix(matrix_m1)
# print()
# print_matrix(matrix_m2)
# print()
# print_matrix(matrix_res)

# """
# Сложение матриц, в общем виде
# как заготовка на будущее
# """
# rows, column = [int(i) for i in input().split()] # количество строк колонок в матрицах
# matrix_a = [[int(i) for i in input().split()] for _ in range(rows)]
# input()
# matrix_b = [[int(i) for i in input().split()] for _ in range(rows)]
#
# matrix_result = matrix = [[0] * column for _ in range(rows)]
#
# for row_index in range(rows):
#     for column_index in range(column):
#         matrix_result[row_index][column_index] = matrix_a[row_index][column_index] + matrix_b[row_index][column_index]
#
# for array in matrix_result:
#     print(*array)

# """
# Заполнение матрицы по спирали...
# 4 5
# 1  2  3  4  5
# 14 15 16 17 6
# 13 20 19 18 7
# 12 11 10 9  8
# """
# по спирали квадратная матрица, есть интересные решенияя,
# N = 5
# a = [None] * N
# for i in range(N): a[i] = [None] * N
# x = 0
# y = 0
# dx = 1
# dy = 0
# for i in range(N * N):
# 	a[y][x] = i + 1
# 	test = x + dx if dx else y + dy
# 	if test < 0 or test == N or a[y + dy][x + dx] != None:
# 		dx, dy = -dy, dx
# 	x += dx
# 	y += dy
#
# for y in range(N): print(a[y])
#
# def next_step(x, y):
#
#     if x == 1:
#         x = 0
#         y = 1
#     elif y == 1:
#         y = 0
#         x = -1
#     elif x == - 1:
#         x = 0
#         y = -1
#     elif y == -1:
#         y = 0
#         x = 1
#     return x, y
#
#
# rows, column = map(int, input().split())
# my_matrix = [[0] * column for _ in range(rows)]
#
# index = 1
# x = 0
# y = 0
# dx = 1
# dy = 0
#
# while index < column * rows + 1:
#     my_matrix[y][x] = str(index).ljust(3)
#     index += 1
#     # проверить следующий шаг. Если достигли края x + dx < 0 или x + dx > column или my_matrix[x + dx][y + dy] == 0
#     if(0 < x + dx > colunm - 1 or 0 < y + dy > rows - 1) or my_matrix[y + dy][x+ dx] != 0:
#         dx, dy = next_step(dx, dy)
#     x = x + dx
#     y = y + dy
#
#
# for row_index in range(rows):
#     print(*my_matrix[row_index])

"""
заполнить заданную матрицу по диагонали
3 5
1  2  4  7  10
3  5  8  11 13
6  9  12 14 15
альтернативное решение
row, colunm = map(int, input().split())
input_value = 1

my_matrix = [[0 for _ in range(colunm)] for _ in range(row)]
for row_index in range(colunm + row - 1):
    for colunm_index in range(row):
        if ((row_index - colunm_index) > -1) and ((row_index - colunm_index) < colunm):
            my_matrix[colunm_index][row_index - colunm_index] += input_value

            input_value += 1

for row_index in range(row):
    print(*my_matrix[row_index])

"""
# def print_matrix(p_matpix):
#     for row_index in range(rows):
#         print(*p_matpix[row_index])
#
# rows, colunm = [int(i) for i in input().split()]
# my_matrix = [[0] * colunm for _ in range(rows)]
# index = 0
# x, y = -1, 1
# while index < rows * colunm:
#
#     while y > 0 and x < colunm - 1:
#         y -= 1
#         x += 1
#         index += 1
#         my_matrix[y][x] = index
#
#     if y == 0 and x < colunm - 1:
#         x += 1
#     else:
#         y += 1
#     index += 1
#     my_matrix[y][x] = index
#
#     while y < rows - 1 and x > 0:
#         y += 1
#         x -= 1
#         index += 1
#         my_matrix[y][x] = index
#
#     if y == rows - 1 and x < 0:
#         x -= 1
#     else:
#         y += 1
#     index += 1
#     my_matrix[y][x] = index
#     print_matrix(my_matrix)
#     print()
# #    break
# #  не работает поворот направо
#
# for row_index in range(rows):
#     print(*my_matrix[row_index])

# """
# поучено два числа
# построить такую матрицу и заполнить по образцу:
# 5 9
# 1 2 3 4 5 6 7 8 9
# 2 3 4 5 6 7 8 9 1
# 3 4 5 6 7 8 9 1 2
# 4 5 6 7 8 9 1 2 3
# 5 6 7 8 9 1 2 3 4
#
# """
# rows, colunm = [int(i) for i in input().split()]
# my_matrix = []  # [[0] * colunm for _ in range(rows)]
#
# for row_index in range(rows):
#     my_matrix.append([])
#     for colunm_index in range(colunm):
#         my_matrix[row_index].append((row_index + colunm_index) % colunm + 1)
#
# for row_index in range(rows):
#     print(*my_matrix[row_index])

# """
# заполнить матрицу нулями, а вехнюю и нижнюю четверти единицами
# """
# # rows, colunm = [int(i) for i in input().split()]
# my_range = int(input())
# my_matrix = [[0] * my_range for _ in range(my_range)]
#
# for row_index in range(my_range):
#     for colunm_index in range(my_range):
#         if colunm_index >= row_index <= my_range - 1 - colunm_index \
#                 or colunm_index <= row_index >= my_range - 1 - colunm_index:
#
#             my_matrix[row_index][colunm_index] = 1
#
# for row_index in range(my_range):
#     print(*my_matrix[row_index])


# """
# В матрице NxM заполнить нулями
# а главную и побочные диагонали заполнить единицами
# """
# # rows, colunm = [int(i) for i in input().split()]
# my_range = int(input())
# my_matrix = [[0] * my_range for _ in range(my_range)]
#
# for colunm_index in range(my_range):
#     for row_index in range(my_range):
#         if row_index == colunm_index or row_index + colunm_index + 1 == my_range:
#             my_matrix[row_index][colunm_index] = 1
#
# for row_index in range(my_range):
#     print(*my_matrix[row_index])


# """
# создать матрицу размером rows строк colunm колонок
# и заполнить значеними с 1 до rows * colunm
# слева направо сверху вниз:
# 3 5
# № строки + 1 +
# 1  4  7  10  13
# 2  5  8  11  14
# 3  6  9  12  15
# """
# rows, colunm = [int(i) for i in input().split()]
# my_matrix = [[0] * colunm for _ in range(rows)]
#
# for colunm_index in range(colunm):
#     for row_index in range(rows):
#         my_matrix[row_index][colunm_index] = str(colunm_index * rows + row_index + 1).rjust(3)
#
# for row_index in range(rows):
#     print(*my_matrix[row_index])

# """
# На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером n×m
# и заполняет её числами от 1 до n*m в соответствии с образцом.
# 3 4
# 1  2  3  4
# 5  6  7  8
# 9  10 11 12
# """
#
# rows, colunm = [int(i) for i in input().split()]
# my_matrix =[]
# value_matrix = [avalue for avalue in range(1, rows*colunm + 1)]
# print(value_matrix)
# current_index = 0
# for row_index in range(rows):
#     my_matrix.append([])
#     for colunm_index in range (colunm):
#         my_matrix[row_index].append(str(value_matrix[current_index]).ljust(3))
#         current_index += 1
#     print(*my_matrix[row_index])
# """
# На вход программе подается натуральное число n.
# Напишите программу, которая создает матрицу размером n×n и заполняет её по следующему правилу:
# числа на побочной диагонали равны 11;
# числа, стоящие выше этой диагонали, равны 00;
# числа, стоящие ниже этой диагонали, равны 22.
# i + j == n -1 # значит заполняем 1
# i +j >= n # значит заполняем 2
# остальное заполняем 0
# """
# my_range = int(input())
# my_matrix = []
# for row_index in range(my_range):
#     my_matrix.append([])
#     for colunm_index in range(my_range):
#         if row_index + colunm_index >= my_range:
#             my_matrix[row_index].append(2)
#         elif row_index +colunm_index == my_range - 1:
#             my_matrix[row_index].append(1)
#         else:
#             my_matrix[row_index].append(0)
#     print(*my_matrix[row_index])


# """
# Шахматная доска
# На вход программе подаются два натуральных числа nn и mm. Напишите программу для создания матрицы
# размером n×m, заполнив её символами . и * в шахматном порядке. В левом верхнем углу должна стоять точка.
# Выведите полученную матрицу на экран, разделяя элементы пробелами.
# """
# x1, x2 = input().split()
# rows, colunm = int(x1), int(x2)    # int(input().split()) #, int(input())
# my_matrix =[]
# for row_index in range(rows):
#     my_matrix.append([])
#     for colunm_index in range(colunm):
#         if (row_index + colunm_index) % 2 == 0:
#             my_matrix[row_index].append(".")
#         else:
#             my_matrix[row_index].append("*")
#
# for row_index in range(rows):
#     print(*my_matrix[row_index])

# """
# Магическим квадратом порядка nn называется квадратная таблица размера n×n, составленная из всех чисел 1,2,3,…,n^2
# так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. Напишите программу,
# которая проверяет, является ли заданная квадратная матрица магическим квадратом.
# 3
# 8 1 6
# 3 5 7
# 4 9 2
# YES
# 3
# 8 2 6
# 3 5 7
# 4 9 1
# NO
# """
#
#
# def check_matrix(in_matrix):
#     len_matrix = len(in_matrix)
#     magic_numbers = [i for i in range(1,  len_matrix**2 + 1)]
#     matrix_numbers = sum(in_matrix, []) # двумерный список в одномерный Ну а потом уже отсортировать и сравнить.
#
#     matrix_numbers.sort()
#     if matrix_numbers != magic_numbers:
#         return False
#
#     # проверить суммы: строк столбцов, диагоналей
#     crc_sum = sum(in_matrix[0])
#     rows_sum = 0
#     gen_diag_sum = 0
#     second_diag_sum = 0
#
#     for row_index in range(len_matrix):
#         if crc_sum != sum(in_matrix[row_index]):
#             return False
#         colunm_sum = 0
#         for colunm_index in range(len_matrix):
#             colunm_sum += in_matrix[colunm_index][row_index]
#             if row_index == colunm_index:
#                 gen_diag_sum += in_matrix[colunm_index][row_index]
#             if colunm_index == len_matrix - row_index - 1:
#                 second_diag_sum += in_matrix[colunm_index][row_index]
#
#         if colunm_sum != crc_sum:
#             return False
#
#     if crc_sum != second_diag_sum != gen_diag_sum:
#         return False
#
#     return True
#
#
# my_range = int(input())
# my_matrix = [[int(i) for i in input().split()] for _ in range(my_range)]
# is_simmetric = check_matrix(my_matrix)
# print("YES" if is_simmetric else "NO")

# """
# На шахматной доске 8×8 стоит конь. Напишите программу, которая отмечает положение коня на доске и все клетки,
# которые бьет конь. Клетку, где стоит конь, отметьте английской буквой N, клетки, которые бьет конь,
# отметьте символами *, остальные клетки заполните точками.
# --------------------
# Чтобы найти все возможные позиции в матрице на которые может пойти конь,
# можно использовать: INX = (x - j) * (y - i) Где x, y - номер строки, столбца на котором находится конь.
# i, j - номер строки, столбца которые проверяются. И если INX = 2 или INX = -2,
# то отмечаем эту позицию (matrix[j][i] = '*')
# """
# # start = input() # пример начального заполнения доски
# # matrix = [['.' for _ in range(8)] for _ in range(8)]  # b6
# # pos_x, pos_y = 8-int(start[1]), ord(start[0])-97
# # matrix[pos_x][pos_y] = 'N'
# # print(*matrix, sep='\n')
# # ------------------ пример
# liter, number = input()
# column_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
# row_dict = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
# RANGE = 8 # размер доски
# my_matrix = []
# x, y = colunm_dict[liter], row_dict[number]
# print(x, y)
# for row_index in range(RANGE):
#     my_matrix.append([])
#     for colunm_index in range(RANGE):
#         my_hit = (x - colunm_index) * (y - row_index)  # Где x, y - номер строки, столбца на котором  находится конь.
#         if row_index == row_dict[number] and colunm_index == colunm_dict[liter]:
#             my_matrix[row_index].append("N")
#         elif my_hit == 2 or my_hit == -2:
#             my_matrix[row_index].append("*")
#         else:
#             my_matrix[row_index].append(".")
# 
# for row_index in range(RANGE):
#     print(*my_matrix[row_index])
# 
# """
# Пример раннего решения про ходы коня
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# 
# out = "NO"
# if (abs(x1 - x2) == 1 and abs(y1-y2) == 2) or(abs(x1 - x2) == 2 and abs(y1-y2) == 1):
#     out = "YES"
# 
# print(out)  
# """

# """
# Дана квадратная матрица чисел.
# Напишите программу, которая поворачивает квадратную матрицу чисел на 90  по часовой стрелке
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# искомый результат
# 7 4 1
# 8 5 2
# 9 6 3
#
# Где было i стало n - j - 1, а там где было j - стало i.
# """
# my_range = int(input())
# my_matrix = [[int(i) for i in input().split()] for _ in range(my_range)]
#
# print("Original")
# for row_index in range(my_range):
#     print(*my_matrix[row_index])
# print("Rotate")
#
# for row_index in range(my_range):
#     for colunm_index in range(my_range):
#         print(my_matrix[my_range - colunm_index - 1][row_index], end=" ")
#     print()


# """
# Дана квадратная матрица чисел. Напишите программу, которая меняет местами элементы,
# стоящие на главной и побочной диагонали, при этом каждый элемент должен остаться в том же столбце
# (то есть в каждом столбце нужно поменять местами элемент на главной диагонали и на побочной диагонали).
# решение
# Проходимся по главной диагонали и помним что, побочная диагональ отличается только первым индексом.
# который можно найти как n-i-1 (-1 так как отсчет с 0). Далее меняем местами и печатаем получившуюся матрицу.
# """
# my_range = int(input())
# my_matrix = [[int(i) for i in input().split()] for _ in range(my_range)]
#
# # for row_index in range(my_range ):
# #     print(f"{str(my_matrix[row_index])} главная: {my_matrix[row_index][row_index]}  "
# #           f"вспомогательная:{my_matrix[my_range - row_index - 1][row_index]}")
#
# for row_index in range(my_range):
#     my_matrix[row_index][row_index], my_matrix[my_range - row_index - 1][row_index] = \
#         my_matrix[my_range - row_index - 1][row_index], my_matrix[row_index][row_index]
#
# for row_index in range(my_range):
#     print(*my_matrix[row_index])

# my_range = int(input())
# my_matrix = [[int(i) for i in input().split()] for _ in range(my_range)]
#
# is_simmetric = True
#
# for row_index in range(my_range):
#     for colunm_index in range(my_range):
#         if colunm_index != row_index:
#             if my_matrix[row_index][colunm_index] != my_matrix[colunm_index][row_index]:
#                 is_simmetric = False
#                 break
#
# print("YES"if is_simmetric else "NO")

# """
# Напишите программу, которая меняет местами столбцы в матрице.
# Программа должна вывести указанную таблицу с замененными столбцами.
# Sample Input 1:
# 3
# 4
# 11 12 13 14
# 21 22 23 24
# 31 32 33 34
# 0 1
#
# Sample Output 1:
# 12 11 13 14
# 22 21 23 24
# 32 31 33 34
# """
# row_range, colunm_range = int(input()), int(input())
# my_matrix = [[int(i) for i in input().split()] for _ in range(row_range)]
# index_changed = [int(i) for i in input().split()]
#
# for row_index in range(row_range):
#     my_matrix[row_index][index_changed[0]],my_matrix[row_index][index_changed[1]] = \
#         my_matrix[row_index][index_changed[1]],my_matrix[row_index][index_changed[0]]
#
# for row_index in range(row_range):
#     for colunm_index in range(colunm_range):
#         print(str(my_matrix[row_index][colunm_index]).ljust(3), end="")
#     print()

# """
# Напишите программу, которая находит индексы (строку и столбец) первого вхождения максимального элемента.
# 3
# 4
# 0 3 2 4
# 2 3 5 5
# 5 1 2 3
# """
# row_range, colunm_range = int(input()), int(input())
# my_matrix = [[int(i) for i in input().split()] for _ in range(row_range)]
#
# row_max_index, colunm_max_index = 0, 0
# max_in_matyrix = my_matrix[row_max_index][colunm_max_index]
# for row_index in range(row_range):
#     for colunm_index in range(colunm_range):
#         if my_matrix[row_index][colunm_index] > max_in_matyrix:
#             max_in_matyrix = my_matrix[row_index][colunm_index]
#             row_max_index, colunm_max_index = row_index, colunm_index
#
# print(row_max_index, colunm_max_index)
# for row_index in range(row_range):
#     for colunm_index in range(colunm_range):
#         print(str(my_matrix[row_index][colunm_index]).ljust(3), end="")
#     print()
# """
# На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрице.
# Создайте матрицу mult размером n×m и заполните её таблицей умножения по формуле mult[i][j] = i * j.
# """
# row_range, colunm_range = int(input()), int(input())
#
# mult = [[str( row_index * colunm_index).ljust(3) for colunm_index in range(colunm_range)] for row_index in range(row_range)]
#
# for rows in range(row_range):
#     print(*mult[rows])
# print(*mult)

# my_range = int(input())
# my_matrix = [[int(i) for i in input().split()] for _ in range(my_range)]
#
# sum_left, sum_up, sum_right, sum_down = 0, 0, 0, 0
# for row in range(my_range):
#     for colunm in range(my_range):
#         if colunm < row < my_range - 1 - colunm: # left
#             sum_left += my_matrix[row][colunm]
#         elif colunm > row < my_range - 1 - colunm: # up
#             sum_up += my_matrix[row][colunm]
#         elif colunm > row > my_range - 1 - colunm: # right
#             sum_right += my_matrix[row][colunm]
#         elif colunm < row > my_range - 1 - colunm: # down
#             sum_down += my_matrix[row][colunm]
#
# print("Верхняя четверть:", sum_up)
# print("Правая четверть:", sum_right)
# print("Нижняя четверть:", sum_down)
# print("Левая четверть:", sum_left)

# my_range = int(input())
#
# my_matrix = []
#
# for c_rows in range(my_range):
#     tmp_matrix = [int(i) for i in input().split()]
#     my_matrix.append(tmp_matrix)
# result = my_matrix[0][0]
# for c_rows in range(my_range):
#     result = max(result, max(my_matrix[c_rows][:c_rows + 1]))
# print(result)


# my_range = int(input())
#
# my_matrix = []
# out_matrix = []
# for c_rows in range(my_range):
#     tmp_matrix = [int(i) for i in input().split()]
#     my_matrix.append(tmp_matrix)
#
# for rows in my_matrix:
#     count_avg = 0
#     for colunms in rows:
#         if colunms > (sum(rows) / my_range):
#             count_avg += 1
#     out_matrix.append(count_avg)
# print(*out_matrix, sep="\n")

# rows, colunms = int(input()), int(input())
# my_matrix = []
# for c_rows in range(rows):
#     in_matrix = []
#     for c_colunms in range(colunms):
#         in_matrix.append(input())
#     my_matrix.append(in_matrix)
#
# for word in my_matrix:
#     print(*word)
# print()
# for c_colunms in range(colunms):
#     for c_rows in range(rows):
#         print(my_matrix[c_rows][c_colunms], end=" ")
#     print()

# in_word = "a b".split() # input().replace(' ', '')
# #in_word = "s t e p i k r o c k s".split() # input().replace(' ', '')
# offset = 0
# result = [[]]
#
# for index in range(1, len(in_word) + 1):
#     i = 0
#     while index + i <= len(in_word):
#         result.append(in_word[i:i + index])
#         i += 1
#
# print(result)

# l = input().split()
# answer = [[]]
# for num in range(1, len(l) +1):
#     i = 0
#     while (num + i) <= len(l) :
#         answer.append(l[i: i+num])
#         i += 1
# print(answer)


# def chunked(in_str, count:int):
#     index = 0
#     ret_list = []
#     while index < len(in_str):
#         ad_list = []
#         for i in range(index, index + count):
#             if i > len(in_str) - 1:
#                 break
#             ad_list.append(in_str[i])
#
#         ret_list.append(ad_list)
#         index += count
#
#     return ret_list
#
#
# in_word =  "a b c d e f r g b" # input().replace(' ', '')
# len_chuncs = 2   # int(input())
# in_word = in_word.replace(' ', '')
# print(chunked(in_word, len_chuncs))


# in_word = input().replace(' ', '')
# #in_word = "w w w o r l d g g g g r e a t t e c c h e m g g p w w"
# #in_word = in_word.replace(' ', '')
# my_list = []
# i = 0
# while i < len(in_word):
#     new_list = list(in_word[i])
#     new_index = i + 1
#     while new_index < len(in_word) and new_list[0] == in_word[new_index]:
#         new_list.append(in_word[new_index])
#         new_index += 1
#     i = new_index
#     my_list.append(new_list)
#
#
# print(my_list)


# in_counter = 4  # int(input())
# my_list = [[1], [1, 1]]  # , [1, 2, 1]]
#
# if len(my_list) < in_counter + 1:  # 3 < 2
#     for i in range(1, in_counter):
#         new_list = [my_list[0][0]]
#
#         for new_i in range(1, len(my_list[i])):
#             new_list.append(my_list[i][new_i - 1] + my_list[i][new_i])
#         new_list.append(1)
#         my_list.append(new_list)
#
# for i in range(len(my_list) - 1):
#     print(*my_list[i])


# in_counter = int(input())
# my_list = list(range(1, in_counter + 1))
# for i in range(1, in_counter + 1):
#     print(my_list[:i])


# in_counter = int(input())
# my_list = []
# for i in range(in_counter):
#     my_list.append([i for i in range(1, in_counter + 1)])
# for i in range(in_counter):
#     print(my_list[i])

"""
# пузырек.
# примитивная сортровка.
получить последовательность из Х чисел
Перемешать shuffle последовательность
отсортировать:
пройти по всем членам последовательности от 2го (индекс = 1) до последнего
сравнить в предыдущим, если он меньше предыдущего то проверить до начала и поменять местами

"""

# from random import shuffle
# array_length = 10
# my_array = list(range(1, array_length + 1))
# shuffle(my_array)
# print(my_array)
# iteration = 0
# for first_index in  range(1, len(my_array)):
#     if my_array[first_index] < my_array[first_index - 1]:
#         second_index = first_index
#         while second_index > 0:
#             if my_array[second_index] < my_array[second_index -1]:
#                 # print(my_array)
#                 iteration += 1
#                 print(my_array[second_index - 1], my_array[second_index])
#                 my_array[second_index - 1], my_array[second_index] =
#                 my_array[second_index], my_array[second_index - 1]
#             else:
#                 break
#             second_index -= 1
# print(f"{my_array} За  {iteration} итераций")

# in_str = input() + " запретил букву"
# rus = [chr(i) for i in range(1072, 1072 + 32)]
# for char in rus:
#     if char in in_str:
#         print(in_str, char)
#         in_str = in_str.replace(char, '').replace('  ', ' ').strip()


# count_device = 6  # = int(input())
# #list_device = [input() for i in range(count_device)]
#
# list_device = ["222anton456", "a1n1t1o1n1", "0000a0000n00t00000o000000n", "gylfole", "richard", "ant0n"]
# numbers_device = []
# for current_index in range(len(list_device)):
#     current_device = list_device[current_index]
#     anton = ["a", "n", "t", "o", "n"]
#     print(current_device)
#     for i in current_device:
#         if i == anton[0]:
#             anton.pop(0)
#             if len(anton) == 0:
#                 numbers_device.append(current_index + 1)
#                 break
#
# print(*numbers_device)

'''
список букв 'anton'
проверка сивола строки с первым из списка, при совпадении удаляем из списка
если список пуст то печатаем и не забываем + 1 и end=' '
'''

# in_string = "ОРРОРОРООРРРО"  # input()
# my_list = in_string.split("О")
# int_list = [len(my_list[i]) for i in range(len(my_list))]
# print(my_list)
# print(max(int_list))

# #  t, r = input(), input()
# t, r = "ящерица", "камень"
#
# magic_dict = {'ножницы': ('бумага', 'ящерица'),
#               'бумага': ('камень', 'Спок'),
#               'камень': ('ножницы', 'ящерица'),
#               'ящерица': ('Спок', 'бумага'),
#               'Спок': ('ножницы', 'камень')}
# if t in magic_dict[r]:
#     print("Руслан")
# elif r in magic_dict[t]:
#     print("Тимур")
# elif r == t:
#     print("ничья")


'''
magic_dict = {'ножницы': ('бумага', 'ящерица'),
              'бумага': ('камень', 'Спок'),
              'камень': ('ножницы', 'ящерица'),
              'ящерица': ('Спок', 'бумага'),
              'Спок': ('ножницы', 'камень')}
прохождение по нему

for key, value in magic_dict.items():
    if s1 in key and s2 in value:
         ***
'''

# t, r = "", ""  # input(), input()
#
# if (t == "камень" and r == "ножницы") or (t == "ножницы" and r == "бумага") or (t == "бумага" and r == "камень"):
#     print("Тимур")
# elif t == r:
#     print("ничья")
# else:
#     print("Руслан")
#
# '''
# если у Тимура камень а у Руслана ножницы - Тимур вин
# если у Тимура ножницы а у Руслана бумага - Тимур вин
# если у Тимура бумага а у Руслана камень - Тимур вин
# если у Тимур = Руслан - ничья
# else:
# Руслан вин.
# '''

# all_len = 6 # int(input()) + 1
# member_set = [33, 17, 35, 999]
#
# # for i in range(all_len):
# #     member_set.insert(len(member_set), int(input()))
#
# result = member_set.pop(-1)
# var_logical = False
# print(member_set)
# check_value = member_set[0]
# for i in range(1, len(member_set)):
#     for current in (member_set[i:]):
#         print(f"{check_value} * {current} = {result} ({check_value * current})")
#         if check_value * current == result:
#             print(f"----{check_value} * {current} = {result} ({check_value * current})")
#             var_logical = True
#     check_value = member_set[i]
#
# print("ДА" if var_logical else "НЕТ")


# in_data = '1 2 3 4 5'  # input()
# in_list = list(map(int, in_data.split()))  # input().split() list(map(int, input().split()))
# inc_len = 0
# while inc_len < len(in_list):
#     print(f"elem: {in_list[inc_len]}  index:{inc_len}")
#     if inc_len % 2 == 1:
#         #print(f"change {in_list[inc_len - 1]} on {in_list[inc_len]}")
#         in_list[inc_len - 1], in_list[inc_len] = in_list[inc_len], in_list[inc_len - 1]
#     inc_len += 1
# print(*in_list)


# in_data = '1 2 3 4 5' # input()
# in_list = input().split()
# #print(in_list)
# int_list = [int(item) for item in in_list]
# counter = 0
# for value in range (1, len(int_list)):
#     if int_list[value] > int_list[value - 1]:
#         counter += 1
#
# print( counter)

# count_input = 4  # int(input())
# list_str_coord = ['0 -1', '1 2', '0 9', '-9 -5']  # [input() for i in range(count_input)]
#
# #print(list_str_coord)
#
# I, II, III, IV = 0, 0, 0, 0
#
# for astr in list_str_coord:
#     x, y = map(int, astr.split())
#     #print(f'x={x} y={y}')
#     if x > 0 and y > 0:
#         I += 1
#     elif x < 0 and  y > 0:
#         II += 1
#     elif x < 0 and  y < 0:
#         III += 1
#     elif x > 0 and y < 0:
#         IV += 1
#
# print(f"Первая четверть: {I}")
# print(f"Вторая четверть: {II}")
# print(f"Третья четверть: {III}")
# print(f"Четвертая четверть: {IV}")


# x, y = map(int, j.split())

# doubled = [thing for thing in list_of_things]
