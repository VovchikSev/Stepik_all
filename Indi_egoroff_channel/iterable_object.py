# 5 Итерируемые объекты и цикл for


# 5.1 Функция range и итерируемые объекты

# 5.2 Цикл for. Обход элементов функции range
# 1
# print(*range(1, int(input()) + 1), sep="\n")
# 2
# print(*range(int(input()) , 0, -1), sep="\n")
# 3
# [ print("Надо было брать биткоин в 2012!") for _ in range(13)]
# 4
# in_str = input()
# in_count = int(input())
# [print(in_str) for _ in range(in_count)]
# 5
# for value in range(int(input()), int(input()) + 1):
#     if value % 3 == 0 and value % 5 == 0:
#         print("FizzBuzz")
#     else:
#         if value % 3 == 0:
#             print("Fizz")
#         elif value % 5 == 0:
#             print("Buzz")
#         else:
#             print(value)
# 6
# for value in range(int(input()), int(input()) + 1):
#     print(f"Число {value}; его квадрат = {value * value}; его куб = {value ** 3}")
# 7
# mishka_score = cris_score = 0
# for value in range(int(input())):
#     mishka, cris = map(int, input().split())
#     if mishka > cris:
#         mishka_score += 1
#     elif cris > mishka:
#         cris_score += 1
#
# print("Mishka" if mishka_score > cris_score else "Chris" if cris_score > mishka_score else "Friendship is magic!^^")

# 8
# my_list = [input().lower() for _ in range(int(input()))]
# for word in my_list:
#     if "рок" in word:
#         print(my_list.index(word) + 1, word.find("рок") + 1)
# print(my_list)

#  9
# recept_list = []
# for _ in range(int(input())):
#     censure = input()
#     if "соль" not in censure:
#         recept_list.append(censure)
# print(*recept_list, sep=", ")

# 10
# result = 0
# for value in range(50, 101):
#     result += value ** 3
# print(result)

# 11
#  слова длиннее 10 заменить
# result_list = []
# for _ in range(int(input())):
#     censure = input()
#     if len(censure) > 10:
#         result_list.append(censure[0] + str(len(censure) - 2) + censure[-1])
#         pass
#     else:
#         result_list.append(censure)
# print(*result_list, sep="\n")
#  короткое, но малопонятное решение. цикл интересен: for w in [input() for _ in range(int(input()))] можно использовать
# # print("\n".join((w, f'{w[0]}{len(w) - 2}{w[-1]}')[len(w) > 10] for w in [input() for _ in range(int(input()))]))

# 5.3 Цикл for. Обход списков и строк
# 1
# in_list = []
# for _ in range(int(input())):
#     in_list.append(input())
# print(in_list)

# 2
# letter = input()
# for word in input().split():
#      if letter in word:
#         print(word)

# 3
# my_list = list(filter(lambda x:x>0, map(int, input().split())))
# print(min(my_list) if len(my_list) > 0 else "Empty")

#  4
# in_str = input().lower()
# print(max(map(lambda x:in_str.count(x), in_str)))

# 5
# in_str = input()
# print("YES" if  (sum(map(int, in_str[::2])) - sum(map(int, in_str[1::2]))) % 11 == 0 else "NO")

# 6
# my_str = list(map(int, filter(lambda value: str(value).isdigit(), input())))
# print(len(my_str), sum(my_str))

# 7
# open = "({["
# close = "}])"
# res = 0
# for char in input():
#     if char in open:
#         res += 1
#     elif char in close:
#         res -= 1
# print("YES" if res == 0 else "NO")
# оптимальный вариант решения
# s = input()
# stack = []
# is_good = True
# for i in s:
#     if i in "({[":
#         stack.append(i)
#     elif i in ")}]":
#         if len(stack) == 0:
#             is_good = False
#             break
#         open_bracket = stack.pop()
#         if open_bracket == "(" and i == ")":
#             continue
#         elif open_bracket == "{" and i == "}":
#             continue
#         elif open_bracket == "[" and i == "]":
#             continue
#         is_good = False
#         break
# print("YES" if is_good and len(stack) == 0 else "NO")
#
# 5.4 Метод подсчета. Сортировка подсчетом Python
# 1
# my_list =  list(map(lambda x:int(x), "11111")) #input()
# val_list = [0] * (max(my_list) + 1)
# for val in my_list:
#     val_list[val] +=1
# for val in range(len(val_list)):
#     if val_list[val] > 0:
#         print(val, val_list[val])
# 2
# incoming_len = int(input()) # совсем ненужный параметр
# my_list = list(map(int, input().split()))
# # len_iteration = (max(my_list) - min(my_list)) + 1
# val_list = [0] * ((max(my_list) - min(my_list)) + 1)  # len_iteration
# my_offset = 0 - min(my_list)
#
# for index in my_list:
#     cur_value = index + my_offset
#     val_list[cur_value] += 1
#
# for index in range(len(val_list)):
#     cur_value = index - my_offset
#     if val_list[index] > 0:
#         print((str(cur_value) + " ") * val_list[index], end="")
# # вместо всего того огорода одна строчка...
# print(*sorted(list(map(int, input().split()))))

# 5.5 Вложенные циклы.
# 1
# Найдите сумму всех четырехзначных чисел, сумма цифр каждого из которых равна 20
# my_sum = 0
# for val in range(1000, 10000):
#     t_val = 0
#     for internal_val in str(val):
#         t_val += int(internal_val)
#     if t_val == 20:
#         my_sum += val
#         print(t_val)
# print(my_sum)
# готовое решение, но нужно вложенные циклы.
# print(sum([x for x in range(1000, 10000) if sum(map(int, list(str(x)))) == 20]))
#
# 2 Программа принимает на вход целое положительное число n (n<=15) - количество уровней, ваша задача вывести n
# уровней, в каждом из которых стоят числа от 1 до значения уровня.
# for val in range(1, int(input()) + 1):
#     print(*list(range(1, val + 1)))
# 3


# def is_prime(in_number):
#     if in_number in (2, 3):
#         return True
#     for val in range(2, int(in_number ** 0.5) + 1):
#         if in_number % val == 0:
#             return False
#     return True
#
#
# number = int(input())
# counter = 0
# for value in range(number + 1,  number * 2 + 1):
#     if is_prime(value):
#         counter += 1
# print(counter)

# сортировка пузырьком
# list_len = int(input())
# my_list = list(map(int, input().split()))
# counter = 0
# for i in range(list_len - 1):
#     for j in range(list_len - i - 1):
#         if my_list[j] > my_list[j + 1]:
#             counter +=1
#             my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
#
# print(*my_list)
# print(counter)

# Сортировка вставкой

# list_len = int(input())
# my_list = list(map(int, input().split()))
# for i in range(len(my_list)):
#     cursor = my_list[i]
#     pos = i
#
#     while pos > 0 and my_list[pos - 1] > cursor:
#         # Меняем местами число, продвигая по списку
#         my_list[pos] = my_list[pos - 1]
#         pos = pos - 1
#     # Остановимся и сделаем последний обмен
#     my_list[pos] = cursor
# print(my_list)

# 5.6 Вложенные списки
# 1
# matrix = [list(map(int, input().split())) for _ in range(int(input())) ]
# my_sum = 0
# for rows_index in range(len(matrix)):
#     for col_index in range(len(matrix[rows_index])):
#         if rows_index == col_index:
#             my_sum += matrix[rows_index][col_index]
# print(my_sum)

# 2
# matrix = [list(map(int, input().split())) for _ in range(int(input())) ]
# for col_index in range(len(matrix[0])):
#     tmp = []
#     for rows_index in range(len(matrix)):
#         tmp.append(matrix[rows_index][col_index])
#     print(*tmp)

# 3
# matrix = [list(map(int, input().split())) for _ in range(int(input())) ]
# for rows_index in range(len(matrix) -1, -1, -1):
#     tmp = []
#     for col_index in range(len(matrix[rows_index]) - 1, -1, -1):
#         # tmp.append(matrix[rows_index][col_index])
#         tmp.append(matrix[col_index][rows_index])
#     print(*tmp)

# 4
# str_len, col_len = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(str_len)]
# for rows_index in matrix:
#     tmp = rows_index.copy()
#     tmp.reverse()
#     print(*tmp)

# 5
# str_len, col_len = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(str_len)]
# for rows_index in range(len(matrix) - 1, -1, -1):
#     print(*matrix[rows_index])

# 6
# matrix = [list(map(int, input().split())) for _ in range(5)]
# for row_index in range(len(matrix)):
#     for col_index in range(len(matrix[row_index])):
#         if matrix[row_index][col_index] == 1:
#             print(abs(2 - row_index) + abs(2 - col_index))
#             break
#
# for row in matrix:
#     print(*row)
#
# 7
#
# str_len, col_len = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(str_len)]
# print(*[sum(value) for value in matrix])
#
# sum_cols = []
# for col_index in range(len(matrix[0])):
#     cur_sum = 0
#     for rows_index in range(len(matrix)):
#         cur_sum += matrix[rows_index][col_index]
#     sum_cols.append(cur_sum)
# print(*sum_cols)

#  8
# matrix = [list(map(int, input().split())) for _ in range(int(input()))]
# flag = True
# for row_index in range(len(matrix)):
#     if not flag:
#         break
#     for col_index in range(len(matrix[row_index])):
#         if row_index != col_index and matrix[row_index][col_index] != matrix[col_index][row_index]:
#             flag = False
#             break
# print('Yes' if flag else 'No')

# 9
# str_len, col_len = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(str_len)]
# result_sum = []
# for value in matrix:
#     result_sum.append(sum(value))
# print(max(result_sum), result_sum.index(max(result_sum)), sep="\n")

# 10
# str_len, col_len = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(str_len)]
# max_val = max(matrix[0])
# max_str = 0
# max_col = matrix[0].index(max(matrix[0]))
#
# for row_index in range(len(matrix)):
#     cur_max = max(matrix[row_index])
#     if cur_max > max_val:
#         max_val = cur_max
#         max_str = row_index
#         max_col = matrix[row_index].index(max(matrix[row_index]))
# print(f"{max_val}\n{max_str} {max_col}")
#
# 11 не решено, сдано в кометах нечто
# str_len, col_len = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(str_len)]
# list_sum = [sum(val) for val in matrix]
# list_max = [max(val) for val in matrix]
# if list_max.count(max(list_max)) == 1:
#     print("значение", *list_max)
#     print(list_max.index(max(list_max)))
# else:
#     print("сумма", *list_sum)
#     print(list_sum.index(max(list_sum)))
# # n, m = map(int, input().split())
# # r, s, i = 0, 0, 0
# # for j in range(n):
# #     a = list(map(int, input().split()))
# #     for b in range(m):
# #         if a[b] > r or (a[b] == r and sum(a) > s):
# #             r, i, s = a[b], j, sum(a)
# # print(i)
#
# 12
# str_len, col_len = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(str_len)]
# list_max = [max(val) for val in matrix]
# print(list_max)
# print(list_max.count(max(list_max)))
#
# 13
# list_wall = []
# for _ in range(4):
#     list_wall.append(list(map(str, input().split())))
# if list_wall[0]==list_wall[1] or list_wall[2]==list_wall[3]:
#     print("No")
# else:
#     print("Yes")
# print(*list_wall, sep="\n")
#
# 14
# str_len, col_len = map(int, input().split())
# in_matrix = [list(input()) for _ in range(str_len)]
# input()
# fix_matrix = [list(input()) for _ in range(str_len)]
# err_count = 0
# for row_index in range(len(in_matrix)):
#     for col_index in range(len(in_matrix[row_index])):
#         if in_matrix[row_index][col_index] == fix_matrix[row_index][col_index]:
#             err_count += 1
# print(err_count)
#
# 15
# str_len, x_value = map(int, input().split())
# count = 0
# for str_index in range(str_len):
#     for col_index in range(str_len):
#         if (str_index + 1) * (col_index + 1) == x_value:
#             count += 1
# print(count)
#
# 5.7 Вложенные списки, Часть 2
#
# 1
# matrix = [list(map(int, input().split())) for _ in range(int(input()))]
# count = 0
# for i in range(len(matrix) - 1):
#     for j in range(i + 1, len(matrix)):
#         if matrix[i][0] == matrix[j][1]:
#             count += 1
#         if matrix[i][1] == matrix[j][0]:
#             count += 1
# print(count)
#
# 2 барьерные элементы
# y_len, x_len = map(int, input().split())
# matrix = ['.' * (x_len + 2)]
#
# for row_index in range(y_len):
#     row = "." + input() + "."
#     matrix.append(row)
# matrix.append('.' * (x_len + 2))
# counter = 0
# for row_index in range(1, y_len + 1):
#     for col_index in range(1, x_len + 1):
#         if matrix[row_index][col_index] == "." and matrix[row_index + 1][col_index] == "." and matrix[row_index][
#             col_index + 1] == "." and matrix[row_index - 1][col_index] == "." and matrix[row_index][col_index - 1] == ".":
#             counter += 1
#
# for row in matrix:
#     print(*row)
# print(counter)
#
#  3
# y_len, x_len = map(int, input().split())
# matrix = []
# start_index = 0
# direction = True
# for row_index in range(y_len):
#     if direction:
#         t_matrix = [value for value in range(start_index, start_index + x_len)]  # от старта к старт + x_len
#     else:
#         t_matrix = [value for value in range(start_index + x_len -1, start_index -1, -1 )]  # от старт + x_len к старт - 1, -1
#     print(*t_matrix)
#     direction = not direction
#     start_index += x_len
#
# 4
# y_len, x_len = map(int, input().split())
# matrix = [input().split() for _ in range(y_len)]
# result = "#Black&White"
# for row_index in range(y_len):
#     for col_index in range(x_len):
#         if matrix[row_index][col_index] in ['C', 'M', 'Y', 'G']:
#             result = "#Color"
#             break
# print(result)
# print(*matrix)
#
# 5 матрица по спирали
# max_value = int(input())
# matrix = [[0] * max_value for _ in range(max_value)]
# index = 1
# y = 0
# x = -1
# d_row = 0
# d_col = 1
# while index <= max_value ** 2:
#     if 0 <= y + d_row < max_value and 0 <= x + d_col < max_value and matrix[y + d_row ][x + d_col] == 0:
#         y += d_row
#         x += d_col
#         matrix[y][x] = index
#         index += 1
#     else:  # повороты
#         if d_col == 1:
#             d_col = 0
#             d_row = 1
#         elif d_row == 1:
#             d_row = 0
#             d_col = -1
#         elif d_col == -1:
#             d_col = 0
#             d_row = -1
#         elif d_row == -1:
#             d_row = 0
#             d_col = 1
# for row in matrix:
#     print(*row)

# 6
#
# y_len, x_len = map(int, input().split())
# matrix = [input() for _ in range(y_len)]
#
# result = [[False] * x_len for _ in range(y_len)]
#
# for row_index in range(y_len):
#     if "S" not in matrix[row_index]:
#         for col_index in range(x_len):
#             result[row_index][col_index] = True
#
# for col_index in range(x_len):
#     is_find = False
#     for row_index in range(y_len):
#         if matrix[row_index][col_index] == "S":
#             is_find = True
#             break
#     if not is_find:
#         for row_index in range(y_len):
#             result[row_index][col_index] = True
# count = 0
# for row in result:
#     count += row.count(True)
# print(count)
