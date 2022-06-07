# Сегодня Роман ждёт в гости своего друга Андрея, чтобы вместе решить контест по программированию.
# Чтобы подготовиться к встрече, Роману необходимо посетить два магазина, расположенных рядом с его домом.
# От дома до первого магазина ведёт дорожка длины d_1 метров, а до второго магазина ведёт дорожка длины d_2 метров.
# Также существует дорожка, соединяющая два магазина друг с другом, длиной d_3 метров.
# https://stepik.org/lesson/666897/step/1?unit=664898
# Напишите программу, которая вычисляет минимальное расстояние, которое потребуется пройти Роману,
# чтобы посетить оба магазина и вернуться домой. Роман всегда стартует из дома. Он должен посетить оба магазина,
# перемещаясь только по имеющимся трём дорожкам, и вернуться назад домой.
# При этом его совершенно не смутит, если ему придётся посетить один и тот же магазин
# или пройти по одной и той же дорожке более одного раза. Единственная его задача —
# минимизировать суммарное пройденное расстояние.

# in_list = [int(input()) for _ in range(3)]
# d_m1, d_m2, m1_m2 = in_list
# all_path = [
#     sum([d_m1, m1_m2, d_m2]),
#     sum([d_m1 * 2, d_m2 * 2]),
#     sum([d_m1 * 2, m1_m2 * 2]),
#     sum([d_m2 * 2, m1_m2 * 2])
# ]
# print(min(all_path))

# Программа должна циклически сдвинуть данный набор чисел на nn шагов и вывести полученный результат,
# разделяя числа символом пробела. Если nn является положительным числом,
# сдвиг происходит вправо, если отрицательным — влево.

# 1 2 3 4 5
# -2
# 3 4 5 1 2

# 1 2 3 4 5
# 1
# 5 1 2 3 4

# in_list = list(map(int, input().split()))
# shift = int(input())
#
# negative = -1 if shift < 0 else 1
# if abs(shift) > len(in_list):
#     # сдвиг больше длинны массива
#     shift = abs(shift) % len(in_list) * negative
#
# print(in_list, shift)
#
# if shift > 0:
#     print(*in_list[-shift:] + in_list[:-shift])
# elif shift < 0:
#     # left = in_list[:-shift]
#     # right = in_list[-shift:]
#     print(*in_list[-shift:] + in_list[:-shift])
# else:
#     print(*in_list)

# my_list[start:stop:step]
# [:] - копия последовательности;
# [::2] - четные элементы последовательности начиная с первого;
# [1::2] - нечетные элементы последовательности начиная со второго;
# [1:] - все элементы, кроме первого;
# [:-1] - все элементы, кроме последнего;
# [1:-1] - все элементы, кроме первого и последнего;
# [::-1] - все элементы в обратном порядке (реверс последовательности);
# [-2:0:-1] - все элементы, кроме первого и последнего, в обратном порядке;
# [-2:0:-2] - каждый второй элемент, кроме первого и последнего, в обратном порядке;


# ru  en
# en_set = set("AaBCcEeHKMOoPpTXxy")
# ru_set = set("АаВСсЕеНКМОоРрТХху")
#
# in_list = []
# for _ in range(3):
#     in_value = input()
#     if in_value in en_set:
#         in_list.append("en")
#     elif in_value in ru_set:
#         in_list.append("ru")
#     else:
#         in_list.append("error")
#
# print(in_list[0] if len(set(in_list)) == 1 else "mix")

# Напишите программу, которая принимает на вход строку текста. И выводит ту же строку
# в одном регистре, который зависит от того, каких букв больше.
# При равном количестве требуется вывести строку в нижнем регистре.

# in_word = input()
# low_counter = 0
# up_counter = 0
# for ch in in_word:
#     if ch.isalpha():
#         if ch.isupper():
#             up_counter += 1
#         else:
#             low_counter += 1
# print(up_counter, low_counter)
# print(in_word.upper() if up_counter > low_counter else in_word.lower())


# def choose_plural(value: int, choose_list: list):
#
#     n2 = value % 100
#     if 11 <= n2 <= 19:
#         return f"{value} {choose_list[2]}"
#     else:
#         n1 = value % 10
#         if n1 == 0 or 5 <= n1 <= 9:
#             return f"{value} {choose_list[2]}"
#         elif n1 == 1:
#             return f"{value} {choose_list[0]}"
#         elif 2 <= n1 <= 4:
#             return f"{value} {choose_list[1]}"
#
#
# print(choose_plural(20021, ['яблоко', 'яблока', 'яблок']))
