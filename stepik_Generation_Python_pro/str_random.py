# import random

# это про Монте - Карло тема интересная, но сильно теоретическая, вытащить в отдельный модуль для отработки.
# попробовать визуализировать
# import numpy as np
# import matplotlib.pyplot as plt
#
# n=1e3
# x = 1-2*np.random.random(int(n))
# y = 1-2.*np.random.random(int(n))
# insideX,  insideY  = x[(x**2+y**2)<=1],y[(x**2+y**2)<=1]
# outsideX, outsideY = x[(x**2+y**2)>1],y[(x**2+y**2)>1]
#
# fig, ax = plt.subplots(1)
# ax.scatter(insideX, insideY, c='b', alpha=0.8, edgecolor=None)
# ax.scatter(outsideX, outsideY, c='r', alpha=0.8, edgecolor=None)
# ax.set_aspect('equal')
# fig.show()  # В Jupyter Notebook не требуется, иначе разкомментируйте
# https://stepik.org/lesson/499669/step/6?unit=491205
# n = 10 ** 7
# k = 0
# s0 = 4 # площадь фигуры
#
# for _ in range(n):
#     x = random.uniform(-1, 1) # диапазон x
#     y = random.uniform(-1, 1) # диапазон y
#
#     if x ** 2 + y ** 2 <= 1: # условие попадания в фигуру
#         k += 1
# print(k)
# print((k / n) * s0)


# def get_symbol(length):
#
#     big_leter = [chr(sym) for sym in range(65, 91)]
#     big_leter.remove("O")
#     big_leter.remove("I")
#     smal_leter = [chr(sym) for sym in range(97, 123)]
#     smal_leter.remove("o")
#     smal_leter.remove("l")
#     digit_symbol = [str(sym) for sym in range(2, 10)]
#     random.shuffle(smal_leter)
#     random.shuffle(big_leter)
#     random.shuffle(digit_symbol)
#     res_list = [smal_leter, big_leter, digit_symbol]
#     ret_str = ""
#     index = 0
#     for i in range(length):
#         if index > 2:
#             index = 0
#         ret_str += res_list[index][random.randint(0, len(res_list[index]) - 1)]
#         index += 1
#     return ret_str
# pasword_count = int(input())
# pasword_len = int(input())
# for _ in range(pasword_count):
#     print(get_symbol(pasword_len))


# # my_list = [input() for _ in range(int(input()))]
# #
# #
# # other_list = my_list.copy()
# # random.shuffle(other_list)
# #
# #
# # for index in range(len(my_list)):
# #     cur_index = other_list.index(other_list[index])
# #
# #     tmp_list = other_list.copy()
# #     tmp_list.remove(my_list[index])
# #
# #     print(f"{my_list[index]} - {tmp_list[0]}")
# # 3
# # Светлана Зуева
# # Аркадий Белых
# # Борис Боков
# # Светлана Зуева - Аркадий Белых
# # Аркадий Белых - Светлана Зуева
# # Борис Боков - Светлана Зуева
# #  этот вариант почему то не принят, утащил похожее из решений
# n = int(input())
# names = [input() for _ in range(n)]
# friends = names.copy()
# random.shuffle(friends)
#
# for i in range(len(names)):
#     print(f"{names[i]} - {names[(i + 1)%len(names)]}")


# простое вычисление факториала
# def factorial(n):
#     res = "*".join([str(i) for i in range(2, n + 1)])
#     return eval(res) if n > 1 else 1
# num = 60
# print(f'\n factorial {num}! = {factorial(num)}')


# my_list = [i for i in range(1, 76)]
# random.shuffle(my_list)
# out_matrix = []
#
# for index_row in range(5):
#     out_matrix.append([])
#     for index_col in range(5):
#         if index_row == 2 == index_col:
#             out_matrix[index_row].append("0".rjust(3))
#         else:
#             out_matrix[index_row].append(str(my_list.pop()).rjust(3))
# for index_row in range(5):
#     print(*out_matrix[index_row])
# for index_col in range(5):
#     print(out_matrix[index_row][index_col])


# print(*out_matrix)
# print(my_list)


# my_list = [ch for ch in input()]
# random.shuffle(my_list)
# print("".join(my_list))

# def gen_num(start):
#     if start:
#         return random.randint(0, 9)
#     else:
#         return random.randint(1, 9)
#
# for series in range(100):
#     gen_number = []
#     for num in range(7):
#         gen_number.append(gen_num(num))
#     print(*gen_number, sep="")

# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
# for index in range(len(matrix)):
#     random.shuffle(matrix[index])
# print(*matrix)


# def generate_index():
#     return chr(random.randrange(65, 90)) + chr(random.randrange(65, 90)) + str(random.randint(0, 100)) + "_" + \
#            str(random.randint(0, 100)) + chr(random.randrange(65, 90)) + chr(random.randrange(65, 90))
#
# print(generate_index())


# def generate_ip():
#     ret_list = []
#     for _ in range(4):
#         ret_list.append(str((random.randint(0, 255))))
#     return ".".join(ret_list)
#
# print(generate_ip())


# numbers = list(range(2, 10, 2))
#
# num = random.choice(numbers)
# print(num)

# res_list = []
# for _ in range(7):
#     res_list.append(random.randint(1, 49))
# print(*sorted(res_list))

# def get_symbol(choise):
#     if choise:
#         return chr(random.randrange(65, 90))
#     else:
#         return chr(random.randrange(97, 122))
#
# length = int(input())    # длина пароля
# for _ in range(length):
#     print(get_symbol(random.choice([1, 0])), end="")


# for _ in range(int(input())):
#     print(random.randrange(1, 7))


# my_list = ["Орел", "Решка"]
# for _ in range(int(input())):
#     print(random.choice(my_list))
