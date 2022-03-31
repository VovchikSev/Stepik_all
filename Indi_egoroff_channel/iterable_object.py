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
