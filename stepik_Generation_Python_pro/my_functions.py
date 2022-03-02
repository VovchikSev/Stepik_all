# word_list = list(input() for _ in range(int(input())))
#
# def get_int_ip(ip):
#     list_ip = ip.split('.')
#     return (int(list_ip[0]) * 256 ** 3) + (int(list_ip[1]) * 256 ** 2) + (int(list_ip[2]) * 256 ** 1) + (int(list_ip[3]) * 256 ** 0)
#
# print(*sorted(word_list, key=lambda ip: get_int_ip(ip)), sep="\n")

# word_list = list(input() for _ in range(int(input())))
#
# def get_geo(word):
#     ret_value = 0
#     for ch in word.upper():
#
#         ret_value += ord(ch) - ord("A")
#     print(ret_value, word)
#     return ret_value
#
# print(word_list)
# word_list.sort()
# print(word_list)
# print(*sorted(word_list, key=lambda wo: get_geo(wo)), sep="\n")



# def arithmetic_operation(operation):
#     func_dict = {"+": lambda x,  y: x + y,
#                  "-": lambda x,  y: x - y,
#                  "*": lambda x,  y: x * y,
#                  "/": lambda x,  y: x / y}
#     return func_dict.get(operation)
#
#
# add = arithmetic_operation('+')
# div = arithmetic_operation('/')
# print(add(10, 20))
# print(div(20, 5))


# def add3(x):
#     return x + 3
#
#
# def mul7(x):
#     return x * 7
#
#
# def compose(f1, f2):
#     return lambda x: f1(f2(x))
#
#
# print(compose(mul7, add3)(1))
# print(compose(add3, mul7)(2))
# print(compose(mul7, str)(3))
# print(compose(str, mul7)(5))


# def mul7(x):
#     return x * 7
#
#
# def add2(x, y):
#     return x + y
#
#
# def add3(x, y, z):
#     return x + y + z
#
# def call(cal_func, *args):
#     return cal_func(*args)
#
#
# print(call(mul7, 10))
# print(call(add2, 2, 7))
# print(call(add3, 10, 30, 40))
# print(call(bool, 0))


# numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12), (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]
#
# sorted_numbers = sorted(numbers, key=lambda x: sum(x) / len(x), reverse=True)
#
# print(sorted_numbers)


# numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
#
# print(*list(filter(lambda x: str(x) != str(x)[::-1], numbers)))
#
# print(*numbers[::-1])


# all_class = []
# all_balls = []
# result = []
# for _ in range(int(input())):
#     all_class.append([input().split() for _ in range(int(input()))])
#
# for val in all_class:
#     all_balls.append(list(map(lambda v: v[1], val)))
#
# for val in all_balls:
#     result.append(bool("5" in val))
#
# # print(*all_class)
# # print(all_balls)
# # print(result)
# print("YES" if all(result) else "NO")


# # Хороший пароль по условиям этой задачи состоит как минимум из 7 символов, содержит хотя бы одну цифру, заглавную и строчную букву
# def any_digit(in_str):
#     ch_digit = bool(len(''.join(i for i in in_str if i.isdigit())) > 0)
#     up_char = False
#     low_char = False
#
#     for ch in in_str:
#         if ch.islower():
#             low_char = True
#             break
#
#     for ch in in_str:
#         if ch.isupper():
#             up_char = True
#             break
#
#     return all([ch_digit, low_char, up_char, bool(len(in_str) > 6)])
#
#
# print("YES" if any_digit(input()) else "NO")

# def chk_val(val):
#     return all(map(lambda v: v > 0 and val % v == 0, map(lambda d: int(d), str(val))))
#
#
# ful_list = [value for value in range(int(input()), int(input()))]
# print(*list(filter(chk_val, ful_list)))
# digits = [int(i) for i in input()]
# print(digits)


# print(all(map(lambda x: x.isdigit() and 0 <= int(x) < 256, list(input().split(".")))))


# abscissas = list(map(float, input().split()))   # x
# ordinates = list(map(float, input().split()))   # y
# applicates = list(map(float, input().split()))  # z
#
# print(all(list(map(lambda val: val[0] ** 2 + val[1] ** 2 + val[2] ** 2 <= 4, list(zip(abscissas, ordinates, applicates))))))


# countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
# capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
# population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]
#
# # all_c = list(zip(countries, capitals, population))
#
# print(*list(map(lambda x: f'{x[1]} is the capital of {x[0]}, population equal {x[2]} people.', list(zip(countries, capitals, population)))), sep='\n')


# # 1  	2 4 3
# #       10	243
# # 2	    1 2 3 4 5 6 7
# #           1	28
# # 3	-2 4 5
# #   3	-1
# # 4	10
# #   2	    10
# # 5	3 19
# #   10	    49
# # 6	10 10 10 10 10
# #   2	            310
# a_list = list(map(int, input().split()))
# x1 = int(input())
#
#
# def evaluate(coefficients, x):
#     list_pow = [val for val in range(len(a_list) - 1, -1, -1)]
#     result = 0
#     for index in range(len(coefficients)):
#         result += coefficients[index] * x ** list_pow[index]
#
#     return result
#
#
# print(evaluate(a_list, x1))
# print(list_pow)
# print(f'{a_list[-1]}*{x} ** 0 = {a_list[-1] * x ** 0}')


# t = a_list + pow_list
# def func(a, b):
#     return a + b
#
# print(reduce(func, t, 0))


# # Противоположные цвета задаются как RGB и (255-R)(255-G)(255-B).
# # вывести противоположный цвет из введенных по формуле
#
# print(*map(lambda x: 255 - int(x), input().split()))

# mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate', 'thursday',
#               76, 70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot', 41,
#               'abort', 13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40, 67, 12, 'abuse', 78,
#               10, 80, 'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51, 95, 'abduct', 37, 98, 99, 14,
#               'abandon', 'accept', 46, 'abide', 'beyond', 19, 'about', 76, 26, 'abound', 12, 95, 'wednesday',
#               'abundant', 'abrupt', 'aboard', 50, 89, 'tuesday', 66, 'bestow', 'absent', 76, 46, 'betray', 47,
#               'able', 11]
# отсортировать: цыфры отсортированные по неубыванию потом слова
# print(sorted(mixed_list, key=lambda x: (not isinstance(x, int), x)))

# mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday',
#               'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271,
#               2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665,
#               'besides', 'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491,
#               'benevolent', 'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643,
#               'aboard', 'bet', 859105, 'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113,
#               1618068, 'berth', 'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant', 2950603,
#               'betray', 'beverage', 'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday', 810387, 'friday',
#               2576799, 2213552, 1599022, 'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197, 2241159,
#               605320, 2347441]
# # Напишите программу, которая с помощью встроенной функции max()
# находит и выводит наибольшее числовое значение в mixed_list.
# print(max(mixed_list, key=lambda value: value if type(value) is int else False))


# Напишите программу его сортировки по возрастанию длины слов, а затем в лексикографическом порядке.
# data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг',
#         'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид',
#         'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']
# print(*sorted(sorted(data), key=lambda word: len(word)))
# # print(*sorted(data, key=lambda x: (len(x), x))) # сразу по двум критериям отсортировано? так можно?

# data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'),
#         (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'),
#         (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'),
#         (7029917, 'Massachusetts'), (6910840, 'Tennessee')]
#
# for stat in sorted(data, key=lambda val: val[1][-1], reverse=True):
#     print(f'{stat[1]}: {stat[0]}')

# numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80,
#            3, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57,
#            53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88,
#            94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
#
# # Напишите программу, которая удаляет из списка numbers все нечетные элементы, большие 47,
# # а все четные элементы нацело делит на два (целочисленное деление – //).
# # Полученные числа следует вывести на одной строке, разделив символом пробела и сохранив исходный порядок.
# # НА ДОСУГЕ ПОПРОБОВАТЬ СДЕЛАТЬ В ОДНУ СТРОКУ
# # print(*map(lambda x: [x // 2, x][x % 2], filter(lambda x: x < 48 or not x % 2, numbers)))
# # print(*map(lambda x: x if x % 2 == 1 else x // 2 , filter(lambda x: '' if x % 2 == 1 and x > 47 else x, numbers)), sep=' ')
#
# new_list = list(filter(lambda value: value % 2 == 0 or value < 47, numbers))
# print(*map(lambda value: value // 2 if value % 2 == 0 else value, new_list))


# words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able',
#          'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow', 'abound',
#          'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday',
#          'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry',
#          'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']
#
# print(*sorted(list(filter(lambda x: len(x) == 6, words))))

# is_non_negative_num = lambda x: x[0].isdigit() and x.count(".") < 2 and set(x).issubset(set("0123456789."))
# print(is_non_negative_num('10.34ab'))
# print(is_non_negative_num('10.45'))
# print(is_non_negative_num('-18'))
# print(is_non_negative_num('-34.67'))
# print(is_non_negative_num('987'))
# print(is_non_negative_num('abcd'))
# print(is_non_negative_num('123.122.12'))
# print(is_non_negative_num('123.122'))


# func = lambda x:  x[0].lower() == x[-1].lower() == 'a'
# print(func('abcd'))
# print(func('bcda'))
# print(func('abcda'))
# print(func('Abcd'))
# print(func('bcdA'))
# print(func('abcdA'))


# выводит в алфавитном порядке список primary городов с населением более 10000000 человек, в формате:
# Cities: Beijing, Buenos Aires, ...

# from functools import reduce
# data = [['Tokyo', 35676000, 'primary'],
#         ['New York', 19354922, 'nan'],
#         ['Mexico City', 19028000, 'primary'],
#         ['Mumbai', 18978000, 'admin'],
#         ['Sao Paulo', 18845000, 'admin'],
#         ['Delhi', 15926000, 'admin'],
#         ['Shanghai', 14987000, 'admin'],
#         ['Kolkata', 14787000, 'admin'],
#         ['Los Angeles', 12815475, 'nan'],
#         ['Dhaka', 12797394, 'primary'],
#         ['Buenos Aires', 12795000, 'primary'],
#         ['Karachi', 12130000, 'admin'],
#         ['Cairo', 11893000, 'primary'],
#         ['Rio de Janeiro', 11748000, 'admin'],
#         ['Osaka', 11294000, 'admin'],
#         ['Beijing', 11106000, 'primary'],
#         ['Manila', 11100000, 'primary'],
#         ['Moscow', 10452000, 'primary'],
#         ['Istanbul', 10061000, 'admin'],
#         ['Paris', 9904000, 'primary']]
# # отсортирован список по первому [0] элементу с наложенным фильтром второй элемент > 10 ** 7
# new_list = sorted(list(filter(lambda x: x[1] > 10 ** 7 and x[2] == "primary", data)), key=lambda x: x[0])
# # извлечены первые элементы в новый список
# result_list = map(lambda val: val[0], new_list)
# print("Cities: " + ", ".join(result_list))
# # не плохое решение
# # cities = filter(lambda city: city[1] > 10 ** 7 and city[2] == 'primary', data)
# # cities = map(lambda city: city[0], cities)
# # cities = sorted(cities)
# # cities = 'Cities: ' + reduce(lambda city1, city2: f'{city1}, {city2}', cities)
# # print(cities)

# # преобразует список floats в список чисел, возведенных в квадрат и округленных с точностью до одного десятичного знака;
# # фильтрует список words  и оставляет только палиндромы длиной более 44 символов;
# # находит произведение чисел из списка numbers
#
# from functools import reduce
# floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
# words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
# numbers = [4, 6, 9, 23, 5]
# # Исправьте этот код
# map_result = list(map(lambda num: round(num ** 2, 1), floats))
# # filter_result = list(filter(lambda name: len(name) > 4, words))
# filter_result = list(filter(lambda name: len(name) > 4 and name == name[::-1], words))
# reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)
#
# print(map_result)
# print(filter_result)
# print(reduce_result)


# # условие в теле анонимной lambda функции
# numbers = [-2, 0, 1, 2, 17, 4, 5, 6]
#
# result = list(map(lambda x: 'even' if x % 2 == 0 else 'odd', numbers))
#
# print(result)


# from functools import reduce
#
# words = ['python', 'stepik', 'beegeek', 'iq-option']
# numbers = [1, 2, 3, 4, 5, 6]
#
# summa = reduce(lambda x, y: x + y, numbers, 0)
# product = reduce(lambda x, y: x * y, numbers, 1)
# sentence = reduce(lambda x, y: x + ' loves ' + y, words, 'Everyone')
#
# print(summa)
# print(product)
# print(sentence)


# words = ['python', 'stepik', 'beegeek', 'iq-option']
#
# new_words1 = list(filter(lambda w: len(w) > 6, words))    #  слова длиною больше 6 символов
# new_words2 = list(filter(lambda w: 'e' in w, words))      #  слова содержащие букву e
#
# print(new_words1)
# print(new_words2)


# strings = ['a', 'b', 'c', 'd', 'e']
# numbers = [3, 2, 1, 4, 5]
#
# new_strings = list(map(lambda x, y: x * y, strings, numbers))
#
# print(new_strings)

# def compare_by_second(point):
#     return point[1]
#
#
# def compare_by_sum(point):
#     return point[0] + point[1]
#
#
# points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]
#
# print(sorted(points, key=compare_by_second))   # сортируем по второму значению кортежа
# print(sorted(points, key=compare_by_sum))      # сортируем по сумме кортежа
# # Очевидно, что такие функции как compare_by_second() и compare_by_sum() не особо нужны вне контекста сорт
#
# points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]
#
# print(sorted(points, key=lambda point: point[1]))                 # сортируем по второму значению кортежа
# print(sorted(points, key=lambda point: point[0] + point[1]))      # сортируем по сумме элементов кортежа

# f1 = lambda: 10 + 20               # функция без параметров
# f2 = lambda х, у: х + у            # функция с двумя параметрами
# f3 = lambda х, у, z: х + у + z     # функция с тремя параметрами
#
# print(f1())
# print(f2(5, 10))
# print(f3(5, 10, 30))

# from operator import add
# from functools import reduce
#
# result = reduce(add, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(result)


# from operator import mul
# result = list(map(mul, ['a', 'b', 'c'], [1, 2, 3]))
# print(result)
# # результат
# # ['a', 'bb', 'ccc']


# # Напишите функцию func_apply(), принимающую на вход функцию и список значений и возвращающую список,
# # в котором каждое значение будет результатом применения переданной функции к переданному списку
#
# def add3(x):
#     return x + 3
#
#
# def mul7(x):
#     return x * 7
#
# def func_apply(func, in_list):
#      return [func(x) for x in in_list]
#
#
# print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
# print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
# print(func_apply(str, [1, 2, 3, 4, 5, 6]))
# # должен выводить:
# #
# # [7, 14, 21, 28, 35, 42]
# # [4, 5, 6, 7, 8, 9]
# # ['1', '2', '3', '4', '5', '6']


# Напишите программу для вычисления и вывода суммы квадратов двузначных чисел, которые делятся на 7 без остатка.
# def two_sim(val):
#      return 9 < abs(val) < 100 and val % 7 == 0
#
# def map(function1, items):
#     result = []
#     for item in items:
#         if function1(item):
#           result.append((item) ** 2)
#     return result
#
# numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58,
#            99, 270, 219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231,
#            178, 201, 260, -35, 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143,
#            43, 297, 229, 60, 254, -9, 5, 187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7,
#            -161, 65, 135, 29, 148, 242, 33, 35, 211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274,
#            73, 197, 272, 54, 278, 26, 280, 13, 171, 2, 79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279,
#            129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234, 10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]
#
# new_numbers = map(two_sim, numbers)
#
# print(sum(new_numbers))


# # Напишите программу для вычисления и вывода суммы квадратов элементов списка
# def reduce(operation, items):
#     ret_val = []
#
#     for val in items:
#         new_item = operation(val)
#         ret_val.append(new_item)
#     return ret_val
#
#
# def oper(value):
#     return value ** 2
#
#
# numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23,
#            35, 11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67,
#            62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29,
#            84, 38, 35, 7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]
# print(*numbers)
#
# new_list = reduce(oper, numbers)
# print(sum(new_list))
# # надо примерно так, в результте print выдал сумму квадротов элементов = 319563
# # def square(x):
# #     return x**2
# #
# # print(sum(map(square, numbers)))

# # Напишите программу, которая с помощью функций filter() и map()
# отбирает из заданного списка numbers трёхзначные числа,
# # дающие при делении на 55 остаток 22, и выводит их кубы, каждый в отдельной строке
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
# def check(item):
#     if 99 < item < 1000:
#         if item % 5 == 2:
#             return True
#     return False
#
# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434,
#            1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289,
#            1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013,
#            898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336,
#            1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]
#
# filter_numbers = filter(check, numbers)
# print(*map(lambda x: x**3, filter_numbers), sep='\n')
# # полное решение до другому
# # def numb(num):
# #     return 99 < num < 1000 and num % 5 == 2
# #
# # def cube(num):
# #     return num**3
# #
# # numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]
# #
# # print(*map(cube, filter(numb, numbers)), sep='\n')


# # Напишите программу, которая с помощью функции map() округляет все элементы списка numbers до 2 десятичных знаков,
# # а затем выводит их, каждый на отдельной строке.
# def function(item):
#     return round(item, 2)
#
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
# numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
#
# # print(*numbers)
# print(*map(function, numbers), sep="\n")
# # без использования своей функции
# # print(*map(lambda x: round(x, 2), numbers), sep='\n')


# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
# numbers = [-2, 45, 45, -7, -45, 37, -42, 27, -58, -58, -12, -27, -49, -27, -56, 4, -99, -11, 86]
#
# var1 = max(numbers, key=abs)
# var2 = min(map(abs, numbers))
#
# print(var1 + var2)

# def sum_digits(val):
#     return sum([int(i) for i in str(val)])
#
# my_list = [int(val) for val in input().split()]
# my_list.sort()
#
# print(*sorted(my_list, key=sum_digits))


# import math
# value, func = int(input()), input()
# def power2():
#      return value ** 2
#
# def power3():
#      return value ** 3
#
# def square():
#           return abs(value) ** 0.5
# def my_abs():
#      return abs(value)
#
# def my_sin():
#      return math.sin(value)
#
# d = {'квадрат': power2,
#      'куб': power3,
#      'корень': square,
#      'модуль': my_abs,
#      'синус': my_sin}
# print(d[func]())
# # аналог с лямбдой
# # from math import sin
# # square = lambda i: i ** 2
# # cube = lambda i:  i ** 3
# # sqrt = lambda i: i ** .5
# # di = {"квадрат": square, "куб": cube, "корень": sqrt, "модуль": abs, "синус": sin}
# # n = int(input())
# # print(di[input()](n))


# my_index = int(input()) - 1
# def get_index_value(value):
#     return value[my_index]
#
# athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
#             ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
# for val in sorted(athletes, key=get_index_value):
#     print(*list(val))


# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100),
#            (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
#
# def my_sum(cort):
#     return max(cort) + min(cort)
#
# print(sorted(numbers, key= lambda c: min(c) + max(c)))
# print(sorted(numbers, key=my_sum))
# print(numbers)


# points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
#
# def length(xy):
#     x, y =xy
#     return (x ** 2 + y ** 2) ** 0.5
# print(sorted(points, key= lambda a:(a[0] ** 2) + a[1] ** 2))
# print(sorted(points, key=length))


# def avg(a):
#     return sum(a) / len(a)
#
# numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,),
#            (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50),
#            (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]
# print(min(numbers, key=avg))
# print(max(numbers, key=avg))
# print(min(numbers, key=lambda x: sum(x)/len(x))) # это верно, функция в строку
# print(max(numbers, key=lambda x: sum(x)/len(x))) # это верно, функция в строку

# min_index = 0
# max_index = 0
#
# for idx in range(len(numbers)):
#     # sum(numbers) / len(numbers)
#     old_sum_min = sum(numbers[min_index])
#     old_sum_max = sum(numbers[max_index])
#
#     if old_sum_min > sum(numbers[idx]) / len(numbers[idx]):
#         min_index = idx
#     if old_sum_max < sum(numbers[idx]) / len(numbers[idx]):
#         max_index = idx
# print(numbers[min_index])
# print(numbers[max_index])

# def info_kwargs(**kwargs):
#     for key, value in sorted(kwargs.items()):
#         print(f"{key}: {value}")
#     [print(f'{key}: {kwargs[key]}') for key in sorted(kwargs.keys())]
# пример данных
# info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')
# def print_products(*args):
#     res_str = [val for val in args if type(val) is str and val != ""]
#     if len(res_str) > 0:
#         for count, val in enumerate(res_str, start=1):
#             print(f"{count}) {val}")
#     else:
#         print("Нет продуктов")
# аналог с условием и выводом в одну строку.
# # def print_products(*args):
# #     ls = [i for i in args if type(i) == str and i not in ('', ' ')]
# #     print('\n'.join([f'{num}) {i}' for num, i in enumerate(ls, 1)]) if ls else 'Нет продуктов')
# # пример данных
# print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)


# def greet(arg1, *args):
#     ret_list = [arg1]
#     if len(args) > 0:
#         ret_list.extend(args)
#     return "Hello " + " and ".join(ret_list) + "!"
# # краcивый аналог
# # def greet(name, *args):
# #     return f'Hello, {" and ".join((name,) + args)}!'
#
# # пример данных
# print(greet('Timur'))
# print(greet('Timur', 'Roman'))
# print(greet('Timur', 'Roman', 'Ruslan'))


# def mean(*args):
#     ret_sum = []
#     for value in args:
#         if type(value) in {int, float}:
#             ret_sum.append(value)
#     if len(ret_sum) == 0:
#         return 0.0
#     else:
#       return sum(ret_sum) / len(ret_sum)
#
# # более красивый и информатиый вариант
# # def mean(*args):
# #     args = [x for x in args if type(x) == int or type(x) == float]
# #
# #     return sum(args) / len(args) if args else 0
# # примеры данных
# print(mean())
# print(mean(7))
# print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
# print(mean(True, ['stepik'], 'beegeek', (1, 2)))
# print(mean(-1, 2, 3, 10, ('5')))
# print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# def matrix(n=1, m=None, value=0):
#     if m is None:  # это ужу выполняется во время вызова функции
#         m = n
#     ret_matrix = []
#     for row_index in range(n):
#         tmp_matrix = []
#         for col_index in range (m):
#             tmp_matrix.append(value)
#         ret_matrix.append(tmp_matrix)
#     return ret_matrix
# print(matrix(3, 5, 3))
