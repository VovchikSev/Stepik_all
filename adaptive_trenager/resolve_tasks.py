# my_list = input().split()
# my_dict = {}
# for word in my_list:
#     my_dict.setdefault(len(word), 0)
#     my_dict[len(word)] += 1
# for len_w, count_w in sorted(my_dict.items()):
#     print(f'{len_w}: {count_w}')
#
# print(my_list)

# def modify_list(l):
#     lst = [i // 2 for i in l if i % 2 == 0]
#     l.clear()
#     l += lst
#
#
# lst = [1, 2, 3, 4, 5, 6]
# print(modify_list(lst))  # None
# print(lst)  # [1, 2, 3]
# modify_list(lst)
# print(lst)  # [1]
#
# lst = [10, 5, 8, 3]
# modify_list(lst)
# print(lst)  # [5, 4]


# # алфавит цезаря
# # https://habr.com/ru/post/552212/ полезная статья в тему, на разбор
# """
# Алгоритм прост, заходит на лету сразу:
# 1. принимаем одну строку как число, вторую как строку
# 2. проходим по всей строке которая будет кодироваться:
#     - для каждого символа снимаем индекс в заданном алфавите(' abcdefghijklmnopqrstuvwxyz')
#     - формируем новую строку - снятый (индекс + шаг) по модулю на длину алфавита.
#     Получаем индекс символа в заданом алфавите.
# 3. вывод новой строки
# """
# def caesar(shift: int, in_str: str):
#     alphabet = " abcdefghijklmnopqrstuvwxyz"
#     result_str = ""
#     for char in in_str:
#         current_index = alphabet.index(char)
#         result_str += alphabet[(current_index + shift) % len(alphabet)]
#     print(f'Result: "{result_str}"')
#
#
# caesar(int(input()), input().strip())


# """
# 1. Кого пугает 1F600—1F64F, поможет int(1F600) и int(1F64F) как начало и конец интервала.
#    Результат будет 128512 и 128591
# 2. Сдвиг может быть как вправо, так и влево, т.е результат после сдвига может быть с кодом 128510 и 128514
# 3. Очень выручил код от Алекса Глозмана: chr(start + (ord(char) - start + offset) % (finish - start + 1)),
#    где start = int(1F600), finish = int(1F64F), offset - это сдвиг.
#    Я долго пытался вспомнить эту формулу для сдвига в обе стороны. О
#    шибки типа Failed test #4 и Failed test #3 возникают как раз из-за ситуаций,
#    в которых выдаваемый вашим кодом символ выходит за рамки 1F600—1F64F
#    chr( start + (ord(char) - start + offset) % (end - start + 1) )
# """
# аналогично цезарю, но с юникодом
# def code_str(shift: int, in_str: str):
#     alphabet = [n for n in range(128512, 128592)]
#     result_str = ""
#     for char in in_str:
#         current_index = alphabet.index(ord(char))
#         result_str += chr(alphabet[(current_index + shift) % len(alphabet)])
#     print(f'Result: "{result_str}"')


# in_str = input() + "-"
# out_str = ''
# # end_index = len(in_str) - 1
# # index = 0
# # counter = 0
# list_w = []
# res_str = ''
# for w in in_str:
#     # если пустая добавить
#     if len(out_str) == 0 or out_str[0] == w:
#         out_str += w
#     else:
#         list_w.append(out_str)
#         out_str = ''
#         out_str += w
#         res_str += f'{len(list_w[-1])}{list_w[-1][0]}' if len(list_w[-1]) > 1 else list_w[-1]
# print(list_w)
# print(res_str)
# aaabccccCCaB

# start = int(input())
#
# if start == 1:
#     print(1)
# else:
#     val = start + 0
#     count = [start]
#     while val > 1:
#         if val % 2 == 0:
#             val = val // 2
#         else:
#             val = 3 * val + 1
#         count.append(val)
#     print(*count)

# my_first_class
# MyFirstClass
# print(''.join([l.title() for l in input().split('_')]))


# my_list = input().lower().split()
# my_dict = {}
# for word in my_list:
#     my_dict.setdefault(word, 0)
#     my_dict[word] += 1
# for key, value in my_dict.items():
#     print(f'{key} {value}')

# in_list = list(map(int, input().split()))
# etalon = int(input())
# out_list = []
# for index in range(len(in_list)):
#     if in_list[index] == etalon:
#         out_list.append(index)
#
# if len(out_list) > 0:
#     print(*out_list)
# else:
#     print("None")


# range = ['6', '7', '8', '9', '1', 'J', 'Q', 'K', 'A']
# first_card, second_card = input().replace("0", "").upper().split()
# super_suit = input().upper()
#
# if first_card[1] == second_card[1]:
#     # масти одинаковые проверить достоинства
#     if range.index(first_card[0]) > range.index(second_card[0]):
#         print("First")
#     elif range.index(first_card[0]) < range.index(second_card[0]):
#         print("Second")
#     else:
#         print("Error")
# else:
#     if first_card[1] == super_suit:
#         print("First")
#     elif second_card[1] == super_suit:
#         print("Second")
#     else:
#         print("Error")
#         # обои две не козырные и масти

# in_value = int(input())
# res_str = []
# index = 1
# while len(res_str) < in_value:
#     res_str += [index for _ in range(index)]
#     index += 1
# print(*res_str[:in_value])

# """
# мили (1 mile = 1609 m),
# ярды (1 yard = 0.9144 m),
# футы (1 foot = 30.48 cm),
# дюймы (1 inch = 2.54 cm),
# километры (1 km = 1000 m),
# метры (m),
# сантиметры (1 cm = 0.01 m)
# миллиметры (1 mm = 0.001 m)
# <number> <unit_from> in <unit_to>
# """
# my_dict = {"mile": 1609, "yard": 0.9144, "foot": 0.3048, "inch": 0.0254, "km": 1000.0,
#            "m": 1.0, "cm": 0.01, "mm": 0.001}
# in_trash = input().split()
# number = float(in_trash[0])
# unit_from = in_trash[1]
# unit_to = in_trash[-1]
# res = (number * my_dict[unit_from]) / my_dict[unit_to]
# print(f"{res:0.2e}")


# """
# https://stepik.org/lesson/3369/step/4?unit=952
# Описание метода.
# вход
# 4 4
# ..*.
# **..
# ..*.
# ....
# выход
# 23*1
# **32
# 23*1
# 0111
# """
# rows, columns = map(int, input().split())
# field_list = [list(map(lambda val: 0 if val == "." else -1, input())) for _ in range(rows)]
#
# for row_index in range(rows):
#     for col_index in range(columns):
#         if field_list[row_index][col_index] == 0:
#             for dy in range(-1, 2):
#                 for dx in range(-1, 2):
#                     y = row_index + dy
#                     x = col_index + dx
#                     if 0 <= y < rows and 0 <= x < columns and field_list[y][x] == -1:
#                         field_list[row_index][col_index] += 1
#
# # for row_index in range(rows):
# #     for col_index in range(columns):
#         cur_val = field_list[row_index][col_index]
#         print("*" if cur_val < 0 else field_list[row_index][col_index], end ="")
#     print()


# """
# Декодировать строку
# 3ab4c2CaB
# промежуточный результат
# 3a b 4c 2C a B
# конечный результат
# aaabccccCCaB
# """
# in_str = ""
# for ch in input():
#     in_str += ch + " " if not ch.isdigit() else ch
# res_list = []
# for current in in_str.split():
#     if len(current) == 1:
#         res_list.append([1, current])
#     else:
#         res_list.append([int(current[:len(current) - 1]), current[-1]])
# for val in res_list:
#     print(val[1] * val[0], end="")
#
# print(res_list)

# фрактал...
# turn_list = ['turn 60', 'turn -120', 'turn 60']
# order = int(input())
# out_str = '.'
# if order <= 1:
#     print(*(turn_list * order), sep='\n')
# else:
#     for angle in range(order):
#         out_str = out_str.replace('.', '.turn 60.turn -120.turn 60.')
#
#     print(*out_str.split('.'), sep='\n')

# """
# Напишите программу, которая принимает на вход список целых чисел, и выводит на экран значения,
# которые повторяются в нём более одного раза.
# """

# # from collections import Counter
# # c = Counter(input().split())
# # print(c)
# # print(' '.join(filter(lambda x: c[x] > 1, c)))
# мое решение не использует модули но немного длиннее.
# my_list = list(map(int, input().split()))
# out_list = []
# for val in my_list:
#     if my_list.count(val) > 1 and val not in out_list:
#         out_list.append(val)
#         print(val, end=" ")


# # охреневшее электронное табло, с нестандартным выводом
# # https://stepik.org/lesson/21306/step/1?adaptive=true&unit=5109
# a1 = ' -- '
# a2 = '|  |'
# a3 = '    '
# a4 = '   |'
# a5 = '|   '
# d = {'0': [a1, a2, a2, a3, a2, a2, a1],
#      '1': [a3, a4, a4, a3, a4, a4, a3],
#      '2': [a1, a4, a4, a1, a5, a5, a1],
#      '3': [a1, a4, a4, a1, a4, a4, a1],
#      '4': [a3, a2, a2, a1, a4, a4, a3],
#      '5': [a1, a5, a5, a1, a4, a4, a1],
#      '6': [a1, a5, a5, a1, a2, a2, a1],
#      '7': [a1, a4, a4, a3, a4, a4, a3],
#      '8': [a1, a2, a2, a1, a2, a2, a1],
#      '9': [a1, a2, a2, a1, a4, a4, a1]}
# in_str = input()
# out_list = []
#
# for index_str in range(7):  # 0 - 6 высота символа, по строкам строим, что выводить
#     created_array = []
#     for index_col in in_str:
#         created_array.append(d[index_col][index_str])
#
#     created_array[0] = "|" + created_array[0]
#     created_array[-1] = created_array[-1] + "|"
#     out_list.append(" ".join(created_array))
#
# print('x'+(len(out_list[0])-2)*'-'+'x')
# print(*out_list, sep="\n")
# print('x'+(len(out_list[0])-2)*'-'+'x')

# def f(x):
#     if x <= -2:
#         return 1 - (x + 2) ** 2
#     elif -2 < x <= 2:
#         return -(x / 2)
#     else:
#         return ((x - 2) ** 2) + 1
# print(f(float(input())))
