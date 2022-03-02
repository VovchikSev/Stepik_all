
# original_str = []
# with open("f:/dataset.txt", 'rt', encoding='utf-8') as my_file:
#     original_str = my_file.readlines()

# my_dict = {}    
# for str_ in original_str:
#     class_, name_, height = str_.strip().split("\t")
#     class_n = int(class_)
#     height = int(height)
#     t_ar = my_dict.get(class_n, [])
#     t_ar.append(height)
#     my_dict[class_n] = t_ar
# max_key = max(my_dict.keys())    
# for val in range(1, max_key + 1):
#     ar = my_dict.get(val, [])
#     if ar == []:
#         print(val, '-')        
#     else:
#         print(val, sum(ar) / len(ar))        
# print(my_dict)


# x, y = 0, 0
# for _ in range(int(input())):
#     vector, val = input().split()
#     if vector == 'север':
#         y += int(val)
#     elif vector == 'юг':
#         y -= int(val)
#     elif vector == 'запад':
#         x -= int(val)
#     elif vector == 'восток':
#         x += int(val)
# print(x, y)
# # через словарь
# n=int(input())
# d={'север':0,'запад':0,'юг':0,'восток':0}
# for i in range(n):
#     x=input().split()
#     d[x[0]]+=int(x[1])
# print(d['восток']-d['запад'], d['север']-d['юг'])

# '''
# движение на восток увеличивает первую координату, а на север — вторую
# 4
# север 10
# запад 20
# юг 30
# восток 40
# '''


# my_dict = {input().lower() for i in range(int(input()))}
# in_text =  {j for i in range(int(input())) for j in input().lower().split(' ')}
# print(*(in_text - my_dict), sep="\n")


# match_list = [input().split(";")  for _ in range(int(input()))]
# command_list = []
# for data_match in match_list:    
#     goals_com_1, goals_com_2 =  int(data_match[1]),  int(data_match[3])    
#     command_list.append([data_match[0], goals_com_1 - goals_com_2])
#     command_list.append([data_match[2], goals_com_2 - goals_com_1])
    
# result_dict = {}
# for match_res in command_list:
#     result_list = result_dict.get(match_res[0],[0, 0, 0, 0]) # [0] - всего игр [1] - побед, [2] - ничьи, [3] - поражения
#     result_list[0] += 1

#     if match_res[1] > 0:
#         result_list[1] += 1

#     elif match_res[1] < 0:
#         result_list[3] += 1

#     elif match_res[1] == 0:
#         result_list[2] += 1

#     result_dict[match_res[0]] = result_list 


# for name_cmd in  result_dict.keys():
#     res_list = result_dict.get(name_cmd)    
#     games = res_list[0]
#     wins = res_list[1]
#     draws = res_list[2]
#     fols = res_list[3]
#     all_result = sum([wins * 3, draws])
#     print(f"{name_cmd}:{games} {wins} {draws} {fols} {all_result}")
 

# '''
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# Результат:
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6
# Команда:Всего_игр Побед Ничьих Поражений Всего_очков
# победа        +3 бала
# ничья          +1 бал
# проигрыш  +0 балов

# '''

# import requests
# start_adres = "https://stepic.org/media/attachments/course67/3.6.3/"
# original_str = ''
# with open("f:/dataset.txt", 'rt', encoding='utf-8') as my_file:
#     original_str = my_file.readline().strip()
# print(original_str)    
# r = requests.get(original_str)


# def open_file(file_name):
#     # req = requests.get(start_adres + file_name)
#     req = file_name
#     counter = 1
#     while True:
#         req = requests.get(start_adres + req).text
#         print(req, counter)
#         counter += 1
#         if req.startswith('We'):
#             return req
            
# open_file(r.text)
# print(r.text)
# краткое решение
# import requests
# url, name = 'https://stepic.org/media/attachments/course67/3.6.3/', '699991.txt'
# while name[:2] != 'We':
#     name = requests.get(url + name).text
# print(name)


# original_str = ''
# with open("f:/dataset.txt", 'rt', encoding='utf-8') as my_file:
#     original_str = my_file.readline().strip()

# unpack_str = ''
# tmp_list = []
# cur_sum = ''
# while len(original_str) > 0:
#     sym = original_str[0]
#     original_str = original_str[1:]
#     chislo = ''
#     index = 0
#     while index < len(original_str) and original_str[index].isdecimal():
#         chislo += original_str[index]
#         index += 1
#     tmp_list.append([sym, int(chislo)])
#     original_str = original_str[index:]

# for arr in tmp_list:
#     unpack_str += arr[0] * arr[1]
# with open("f:/out.txt", 'w', encoding='utf-8') as out_file:    
#     print(unpack_str, file=out_file)    


# my_list = []
# while True:
#     in_str = input()
#     if in_str == 'end':
#         break
#     else:
#         my_list.append([int(value) for value in in_str.split()])

# out_list = []

# def count_value(x:int, y:int)->int:
#     x_left = x - 1
#     x_right =  0 if x >= len(my_list[0]) - 1 else x + 1
#     y_up = y - 1
#     y_down = 0 if y >= len(my_list) - 1 else y + 1
#     return my_list[y][x_left] + my_list[y][x_right] + my_list[y_up][x] + my_list[y_down][x]
    
# for row in range(len(my_list)):
#     generated_list = []
#     for col in range(len(my_list[row])):
#         generated_list.append(count_value(col, row)) # col = x столбцы; row = y строки
#     out_list.append(generated_list)
# for value in out_list:
#     print(*value)



# in_list = [int(value) for value in input().split()]
# quest = int(input())
# list_index = []
# if quest not in in_list:
#     print("Отсутствует")
# else:    
#     for index in range(len(in_list)):
#         if in_list[index] == quest:
#             list_index.append(index)
#     print(*list_index)



# num = int(input())
# num_list = [val for val in range(1, num + 1)]
# out_list = []
# for value in num_list:
#     str_value = [int(n) for n in ((str(value) + " ") * value).split()]    
#     for add_v in str_value:
#         out_list.append(add_v)
#     if len(out_list) > num:
#         break

# print(*out_list[:num])


# my_list = []
# my_sum = 0
# while True:
#     value = int(input())
#     my_list.append(value)
#     my_sum += value
#     if my_sum == 0:
#         break
# print(sum(map(lambda value: value ** 2, my_list)))


# сапер поле, с расстановкой
# x_len, y_len, mines = (int(i) for i in input().split())  # чтение размеров поля и числа мин
# fild_list = [[0 for y in range(y_len)] for x in range(x_len)]  # заполнение поля нулями

# def count_mine(x:int, y:int):
#     for dx in range(-1, 2):
#         for dy in range(-1, 2):
#             ax = x + dx
#             ay = y + dy
#             if 0 <= ax < x_len and 0 <= ay < y_len and fild_list[ax][ay] == -1:
#                 fild_list[x][y] += 1



# # расставляем мины
# for _ in range(mines):
#     row, col = (int(i) - 1 for i in input().split())
#     fild_list[row][col] = -1
# # расчет поля 
# for x in range(x_len):
#     for y in range(y_len):
#         if fild_list[x][y] == 0: # для таких полей расчитать значение -1 в соседях
#             count_mine(x, y)

# # вывод результата
# for row in fild_list:
#     for col in row:
#         if col == -1:
#             print("*", end="")
#         elif col == 0:
#             print(".", end="")           
#         else:
#             print(col, end="")            
#     print()
# '''
# 5 4 4 
# 1 1
# 2 2
# 3 2
# 4 4
# '''


# one_prog = [1, 21, 31, 41, 51, 61, 71, 81, 91]
# two_prog = [2, 3, 4]
# prog_amount = int(input())
# if prog_amount > 99:    
#     calc_amount = prog_amount % ((prog_amount // 100) * 100)
# else:
#     calc_amount = prog_amount

# if calc_amount in one_prog:
#     prog_str = 'программист'
# elif calc_amount in two_prog or (calc_amount % 10 in two_prog and calc_amount > 20):
#     prog_str = 'программиста'
# else:
#     prog_str = 'программистов'
# print(f'{prog_amount} {prog_str}')



# sum_credit = int(input()) # s
# mounths_count = int(input()) # n
# percents = int(input()) # k

# ka = percents / 1200
# ka_1_n = (1 + ka) ** mounths_count

# pa = (ka * ka_1_n /(ka_1_n - 1)) * sum_credit

# def diference(mounth:int)->float:    
#     s_n = sum_credit / mounths_count
#     return s_n + (sum_credit - (mounth - 1) * s_n) * ka

# cabbala = 0
# for mounth_num  in range(1, mounths_count + 1):
#      pay = diference(mounth_num)
#      print(f"{mounth_num:2d} месяц - (диф.) {pay:8.2f} руб - (анн.) {pa:8.2f} руб") # "%2d месяц - %8.2f руб"
#      cabbala += pay# def mounth_pay(mounth_num, mounths, sum_credit, percent):
     
# print(f"Доход банка - (диф.) {(cabbala - sum_credit):6.2f} руб - (анн.) {((pa * mounths_count) - sum_credit):6.2f} руб")



# # Известны величины потребленной электроэнергии в некотором помещении  за каждый месяц года. 
# # Месячная норма потребления электроэнергии n кВт·ч , стоимость 1 кВт·ч в пределах нормы  a руб, 
# # и стоимость за каждый 1 кВт·ч потребления электроэнергии сверх нормы  b руб.  
# # Вычислите суммарное потребление и стоимость электроэнергии за год. https://stepik.org/lesson/267960/step/3?unit=248937
# mounths = list(map(int, input().split())) 
# mounth_norm = int(input())
# norm_cost = float(input())
# over_cost = float(input())

# mounth_cost = []
# for mounth in mounths:
#     if mounth > mounth_norm:
#         norm = mounth_norm * norm_cost
#         over_morm = (mounth - mounth_norm) * over_cost
#         mounth_cost.append(over_morm + norm)

#     else:
#         mounth_cost.append(mounth * norm_cost)   

# print(f"Сумма: {sum(mounths):6d} кВт ч, стоимость {sum(mounth_cost):7.2f} руб")


# # Даны n населенных пунктов, каждый из которых в некоторой относительной системе координат имеет две координаты x и y. 
# # В пункте с номером (индексом) k установлена радиостанция с радиусом действия  r км. Определить, 
# # сколько населенных пунктов попадает в радиус ее действия  (включая населенный пункт k).
# # чтение входных данных
# x_list = list(map(int, input().split())) # список координат Х (строка, в которой через пробел перечислены координаты населенных пунктов по оси OX)
# y_list = list(map(int, input().split())) # список координат У (трока, в которой через пробел перечислены координаты населенных пунктов по оси OY)
# city_index = int(input()) # индекс координат города с радиостанцией в спискакх координат (индекс есть в списках координат)
# distance = int(input()) # радиус действия радиостанции
# #  требуется только вывести те у которых растояние от city_index мньше или равно distance
# def is_in_distance(x1:int, y1:int, x2:int, y2:int) ->bool:
#     '''
#     Args:
#         Координаты БС (x1, x2)   
#         Координаты города (x2, y2)
#     Returns:
#         True if the coordinates of the settlement 
#         are within the range of the radio station. 
#         Otherwise False
#     '''
#     return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 <= distance

# in_distance = [] # списсок 
# for index in range(len(x_list)):
#     if is_in_distance(x_list[city_index], y_list[city_index], x_list[index], y_list[index]):
#         in_distance.append(tuple([x_list[index], y_list[index]]))
# print(in_distance)
# print(len(in_distance))

# # пример реализации с визуализацией на графике
# # X = input() раскомментировать для реальной задачи
# # Y = input() раскомментировать для реальной задачи
# # k = input() раскомментировать для реальной задачи 
# # r = input() раскомментировать для реальной задачи

# X = '27 53 44 88 35 86 92 20 10 73 81' # Замемментировать
# Y = '97 22 57 58 37 55 34 29 80 55 71' # Замемментировать
# k = '7' # Замемментировать
# r = '68' # Замемментировать

# import numpy as np
# from matplotlib.patches import Circle
# import matplotlib.pyplot as plt

# towns = np.array(list(zip(list(map(int, X.split())), list(map(int, Y.split())))))
# k = int(k)
# r = int(r)

# distances = np.linalg.norm(towns - towns[k], ord=2, axis=1)

# towns_True = towns[(distances <= r)]
# towns_False = towns[(distances > r)]

# n = np.amax(towns, axis = 0)[0] + 5
# m = np.amax(towns, axis = 0)[1] + 5 
# plt.xlim(0, n)
# plt.ylim(0, m)
# ax = plt.gca()
# ax.set_aspect(1)

# figure_c = Circle((towns[k]), r, fill=False)
# ax.add_patch(figure_c)
# punkt_Yes = plt.plot(towns_True[:, 0], towns_True[:, 1], '+', color='xkcd:green', label = "Radio-ON")
# punkt_No = plt.plot(towns_False[:, 0], towns_False[:, 1], 'x', color='xkcd:red', label = "Radio-OFF")
# punkt_k = plt.plot(towns[k][0], towns[k][1], '*', color='xkcd:blue', label = "k" )
# plt.title('Карта покрытия')

# plt.grid()
# plt.legend()
# plt.show()


# t_0 = list(map(float, input().split()))
# t_12 = list(map(float, input().split()))
# avg_t = float(input())

# for index in range(len(t_0)):
#     if (t_0[index] + t_12[index]) / 2 > avg_t:
#         print(index)


# from math import atan, pi

# def earth_population(t):        
#     return 172 / 45 * (pi/2-atan((2000-t)/45))

# years = [1000, 1750, 1800, 1850, 1900, 1950, 1955, 
#          1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 
#          2000, 2005, 2010, 2011, 2012, 2013, 2014, 2015,
#          2016, 2017, 2018, 2019]

# population =[0.400, 0.791, 1.000, 1.262, 1.650, 2.519,
#              2.756, 3.021, 3.335, 3.692, 4.068, 4.435, 4.831,
#              5.264, 5.674, 6.071, 6.344, 6.933, 7.015, 7.100,
#              7.162, 7.271, 7.358, 7.444, 7.530, 7.669, 7.763] 

# first_index = int(input())
# last_index  = int(input())

# main_years = years[first_index:(last_index + 1)]
# main_population = population[first_index:(last_index + 1)]

# main_earth_population = [earth_population(value) for value in main_years]


# error_list = [abs((main_earth_population[index] - main_population[index]) / main_population[index]) for index in range(len(main_years))]

# min_error_index = error_list.index(min(error_list))
# max_error = error_list.index(max(error_list))
# avg_error = sum(error_list) / len(error_list) * 100

# print(f"Погрешность - минимальная, год: {main_years[min_error_index]:4d}, максимальная, год: {main_years[max_error]:4d}, средняя, процент: {avg_error:6.3f}")

# def compute_lambda(t):
#     # Создать функцию compute_lambda(t) для вычисления теплопроводности:
#     b = 33
#     l_0 = 884
#     t_0 = 100
#     y = b * l_0 / (t-t_0)
#     return y


# # Создать пустые списки для значений температур и теплопроводности:
# t_list = []
# lambda_exp_list = []

# #  входные данные для проверки,
# f = '''200 264
# 300 148
# 400 98.2
# 500 76.2
# 600 61.3
# 700 50.8
# 800 42.2
# 900 35.9
# 1000 31.2
# 1100 28.5
# 1200 25.7
# 1300 24.6
# 1400 23.5
# 1500 22.8
# 1600 22.1'''

# # Замена чтению из файла
# f = f.split('\n')

# # Первый элемент списка t_lambda_listдобавить к списку температур, второй – к списку теплопроводности,
# # преобразовав строковое значение к вещественному.
# for line in f:
#     t_lambda_list = line.split()
#     t_list.append(float(t_lambda_list[0]))
#     lambda_exp_list.append(float(t_lambda_list[1]))

# # Сформировать список со значениями теплопроводности, посчитанными с помощью функции compute_lambda(t) для температур
# lambda_list = [compute_lambda(t) for t in t_list]
# error_list = [abs((lambda_exp_list[i] - lambda_list[i]) /
#                   lambda_exp_list[i]) for i in range(len(t_list))]

# # Cформировать таблицу вывода значений температур, экспериментально полученной теплопроводности, 
# # рассчитанной по формуле теплопроводности и погрешности вычислений..
# print("-" * 40)
# print("|%7s | %7s | %7s |%8s |" % ("t","l(t)","exp(t)", "error"))
# print( "-" * 40)
# for i in range(len(t_list)):
#     print("|%7d | %7.3f | %7.1f |%7.2f%% |"
#           % (t_list[i], lambda_list[i], lambda_exp_list[i], error_list[i] * 100))

# print("-" * 40)                   

# # Найти максимальную погрешность, указать какой температуре она соответствует. Для этого :
# # - вычислить максимальную погрешность
# max_error = max(error_list)
# index_max_error = error_list.index(max_error)
# print("Максимальная погрешность = %5.2f%%  при t = %5d"% (max_error * 100, t_list[index_max_error]))

# # Аналогично вычислить минимальную погрешность:
# min_error = min(error_list)
# index_min_error = error_list.index(min_error)
# print("Минимальная погрешность = %5.2f%%  при t = %5d"% (min_error * 100, t_list[index_min_error]))

# # Найти среднюю погрешность:
# avg_error = sum(error_list) / len(t_list)
# print("Средняя погрешность = %5.2f%%" % (avg_error * 100))


# def mounth_pay(mounth_num, mounths, sum_credit, percent):
#     return (sum_credit / mounths) + (sum_credit - (mounth_num - 1) * (sum_credit / mounths)) * (percent / 1200)

# sum_credit = int(input())
# mounths = int(input())
# percent = int(input())

# cabbala = 0
# for mounth_num  in range(1, mounths + 1):
#     pay = mounth_pay(mounth_num, mounths, sum_credit, percent)
#     print(f'{mounth_num} - месяц {pay:8.2f} руб') # "%2d месяц - %8.2f руб"
#     cabbala += pay

# print(f'Доход банка - {(cabbala - sum_credit):6.2f} руб')

'''
Когда в ясный день обхожу я жилище почтенной матронны,
Родившей супругу мою, что изгибами стана способна затмить Афродиту.
Стремлюсь показать, сколь искусен я в жанре комедии.
Просунув могучий приап, сквозь витую ограду.
Иль дерзко явить афедрон цвета бронзы, на фоне колонн белоснежных.
'''

# # рисование на графике не простого кота, бесполезная но симпатичная штука
# from matplotlib.patches import Circle, Wedge, Polygon, Ellipse, Arc, Path, PathPatch
# import matplotlib.pyplot as plt

# def draw_cat(ax):
#  # туловище
#     poly = [(3, 1), (4, 14), (5, 11), (8, 11), (9, 14), (10, 1)]
#     polygon = Polygon(poly, fc="grey", ec="black", lw=4)
#     ax.add_patch (polygon)

#     # глаза
#     circle = Circle((5.3, 8.5), 1.2, fc="white", ec="black", lw=4)
#     ax.add_patch (circle)

#     circle = Circle((7.7, 8.5), 1.2, fc="white", ec="black", lw=4)
#     ax.add_patch (circle)

#     # зрачки
#     circle = Circle((6, 8.3), 0.1, fc="black", ec="black", lw=4)
#     ax.add_patch (circle)

#     circle = Circle((7, 8.3), 0.1, fc="black", ec="black", lw=4)
#     ax.add_patch (circle)

#     # нос
#     circle = Circle((6.5, 7.5), 0.3, fc="black", ec="black", lw=4)
#     ax.add_patch (circle)

#     # задние лапы
#     wedge = Wedge((3, 1), 2, 86, 180, fc="grey", ec="black", lw=4)
#     ax.add_patch (wedge)

#     wedge = Wedge((10, 1), 2, 0, 94, fc="grey", ec="black", lw=4)
#     ax.add_patch (wedge)

#     # передние лапы
#     ellipse = Ellipse((5.5,1.2), 2, 1.5, fc="grey", ec="black", lw=4)
#     ax.add_patch (ellipse)

#     ellipse = Ellipse((7.5,1.2), 2, 1.5, fc = "grey", ec="black", lw=4)
#     ax.add_patch (ellipse)

#     # улыбка
#     arc =  Arc((6.5, 6.5), 5, 3, 0, 200, 340, lw=4, fill=False)
#     ax.add_patch(arc)

#     # линия между носом и улыбкой, усы
#     vertices = [(6.5, 5), (6.5, 7.5), (10, 6), (6.5, 7.5), (10, 6.5), (6.5, 7.5), (10, 7),
#                 (6.5, 7.5), (3, 6), (6.5, 7.5), (3, 6.5), (6.5, 7.5), (3, 7)]

#     # число 1 соответствует команде matplotlib.path.Path.MOVETO
#     # число 2 соответствует команде matplotlib.path.Path.LINETO
#     codes = [1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]

#     path = Path(vertices, codes)
#     path_patch = PathPatch(path, fill=False, lw=1)
#     ax.add_patch(path_patch)

# # Установить размер и координаты углов для области рисования - должны соответствовать рисунку:
# n = 13
# m  = 15

# plt.xlim(0, n)
# plt.ylim(0, m)

# # Создать область, связанную с осями координат, куда будут выводиться плоские фигуры (ax),
# # вызвать функцию рисования (draw_cat):
# ax = plt.gca()
# draw_cat(ax)

# # Удалить оси координат и показать рисунок:
# ax.axes.set_axis_off()
# plt.show()


# import matplotlib.pyplot as plt
# from math import sin, cos, log, pi, radians, exp

# def f_x(x):
#    return exp(cos(radians(x))) + log(sin(radians(0.8*x))**2 + 1)*cos(radians(x))

# def f_y(x):
#     return -log( (cos(radians(x)) + sin(radians(x)))**2 + 1.7) + 2

# # def my_radian(gradus):
# #     return (gradus * pi) / 180

# # def my_gradus(radian):
# #     return (radian * 180) / pi

# a = -240
# b = 360
# n = 100

# h = (b-a)/(n-1)

# print(f_x(71), f_y(71))
# f_list = [a + h * i for i in range(n)]

# x_list = [f_x(x) for x in f_list]
# y_list = [f_y(x) for x in f_list]


# # Построить линии графиков функций, зададим подпись для вывода легенды:
# line_f = plt.plot(f_list, x_list, label='f(x)')
# line_y = plt.plot(f_list, y_list, label='y(x)')

# # Задать стили линий:
# plt.setp(line_f, color="blue", linewidth=2)
# plt.setp(line_y, color="red", linewidth=2)
# # Вывести 2 оси, установим для них позицию zero:
# plt.gca().spines["left"].set_position("zero")
# plt.gca().spines["bottom"].set_position("zero")
# plt.gca().spines["top"].set_visible(False)
# plt.gca().spines["right"].set_visible(False)
# # Вывести легенду и заголовок в область построения:
# plt.legend()
# plt.title("Графики функций")
# # Отобразить область построения:
# plt.show()


# import matplotlib.pyplot as plt

# def f_x(x):
#    y = x ** 3 - 6 * x ** 2 +  x + 5
#    return y

# def y_x(x):
#     y = (x - 2) ** 2 -6
#     return y

# # Зададать интервал построения функции и количество точек построения. Вычислим шаг:
# a = -2
# b = 6
# n =100
# h = (b-a)/(n-1)

# # Сформировать списки со значениями аргументов и значениями функций в них:
# x_list = [a + h * i for i in range(n)]
# f_list = [f_x(x) for x in x_list]
# y_list = [y_x(x) for x in x_list]

# # Построить линии графиков функций, зададим подпись для вывода легенды:
# line_f = plt.plot(x_list, f_list, label='f(x)')
# line_y = plt.plot(x_list, y_list, label='y(x)')

# # Задать стили линий:
# plt.setp(line_f, color="blue", linewidth=2)
# plt.setp(line_y, color="red", linewidth=2)

# # Вывести 2 оси, установим для них позицию zero:
# plt.gca().spines["left"].set_position("zero")
# plt.gca().spines["bottom"].set_position("zero")
# plt.gca().spines["top"].set_visible(False)
# plt.gca().spines["right"].set_visible(False)

# # Вывести легенду и заголовок в область построения:
# plt.legend()
# plt.title("Графики функций")

# # Отобразить область построения:
# plt.show()


# разобраться с построением графика перечитав результаты решений по образцам
# import matplotlib.pyplot as plt
# from math import atan , pi
# # https://stepik.org/lesson/267709/step/6?unit=248684
# # что решаем
# def f_x(x):
#    y = (172/45)*((pi/2)-atan(((2000 - x)/45)))
#    return y

# plt.gca().spines["left"].set_position("center")
# plt.gca().spines["bottom"].set_position("center")
# plt.gca().spines["top"].set_visible(False)
# plt.gca().spines["right"].set_visible(False)

# x_list = []
# y_list = []

# year_start = 2025
# year_finish = 2027

# for x_value in range(year_start, year_finish + 1):
#     x_list.append(x_value)
#     cur_y = f_x(x_value)
#     if cur_y * 10 ** 9 >= 8 * 10 ** 9:
#         print(x_value, cur_y)
#     print(cur_y, round(cur_y), x_value)
#     y_list.append(cur_y)

# #функция создания линии
# plt.plot(x_list, y_list, "r+-")
# plt.show()


# import matplotlib.pyplot as plt
# def f_x(x):
#    y = x ** 3 - 6 * x ** 2 +  x + 5
#    return y

# a = -2
# b = 6
# n =100
# h = (b-a)/(n-1)

# x_list = [a + h * i for i in range(n)]
# f_list = [f_x(x) for x in x_list]

# line = plt.plot(x_list, f_list)

# plt.setp(line, color="blue", linewidth=2)
# plt.gca().spines["left"].set_position("zero")
# plt.gca().spines["bottom"].set_position("zero")
# plt.gca().spines["top"].set_visible(False)
# plt.gca().spines["right"].set_visible(False)
# plt.show()

# from math import atan, pi

# def earth_population(t):
#     Nt = 172 / 45 * (pi / 2 - atan((2000 - t) / 45))
#     return Nt

# line = input()
# years_str_list = map(int, line.split())

# for t in years_str_list:

#     Nt = earth_population(t)

#     print("%5d - %6.3f миллиард(ов)" % (t, Nt))


# # Дано значение времени в 12-ти часовом формате h:m:s.
# # Определить угол в градусах между положением часовой стрелки в начале суток
# # и ее положением в h часов, m минут и s секунд.

# hours, minutes, seconds = int(input()), int(input()), int(input())
# if hours not in range(12) or minutes not in range(60) or seconds not in range(60):
#     print('error')
# else:
#     angle = hours * 30 + minutes * 0.5 + seconds * (0.5/60)
#     print(round(angle, 2))


# a = float(input())
# ''' сторона бассейна'''

# b = float(input())
# ''' расход краски - милилитров на метр квадратный '''

# v = int(input())
# ''' объем банки с краской '''

# # проверка ошибочных данных
# '''
# a <= 0
# b <= 0
# v < 1
# '''
# def rashod(all_s, on_one_quadre_v, bootle_v):
#     bootles = all_s * on_one_quadre_v / bootle_v
#     return int(bootles) if int(bootles) - bootles == 0 else int(bootles) + 1

# if a <= 0 or b <= 0 or v < 1:
#     print('error')
# else:
#     print(rashod((a * a) * 5, b, v * 1000))


# one_ruble = [1, 21, 31, 41, 51, 61, 71, 81, 91]
# two_ruble = [2, 3, 4]

# rub = int(input())
# if rub < 1 or rub >99: # 1<=n<=99
#     print("error")
# else:
#     if rub in one_ruble:
#         rub_str = 'рубль'
#     elif rub in two_ruble or (rub % 10 in two_ruble and rub > 20):
#         rub_str = 'рубля'
#     else:
#         rub_str = 'рублей'
#     print(f'{rub} {rub_str}')

# # интересное решение,
# # выбирается из списка слов по остатку от деления, последняя цифра и обход второго десятка сделан ловко.
# # Раобраться детально в решении
# # k = int(input())
# # rub_list = [" рублей", " рубль", " рубля", " рубля"," рубля", " рублей", " рублей", " рублей", " рублей", " рублей"]
# # if 1 <= k <= 99:
# #     if 10 < k < 20:
# #         print(str(k) + rub_list[0])
# #     else:
# #         print(str(k) + rub_list[k%10])
# # else:
# #     print('ошибка')


# def get_days(year):
#     if year < 1582:
#         return 'error'
#     else:
#         # return 366 if  (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 365
#         return 365 + __import__('calendar').isleap(year)

# print(get_days(int(input())))

# a = float(input())
# h = float(input())


# if a > 0 and h > 0:
#     v = (a ** 2 * h) / (4 * (3 ** 0.5))
#     s1 = (a ** 2 * (3 ** 0.5)) / 4
#     s2 = (3 * a) / 2
#     s3 = (h ** 2 + (a ** 2 / 12)) ** 0.5
#     s = s1 + s2 * s3
#     print(round(v, 3), round(s, 3))
# else:
#     print('error')

# # # то же самое через класс
# # class Pyramid:
# #     def __init__(self, a, h):
# #         #  прверка корректности данных  a и h должны быть больше нуля
# #         self.a = False if a <= 0 else a
# #         self.h = False if h <= 0 else h
# #         self.correct = self.a and self.h

# #     def get_V(self):
# #         '''метод вычисления объема'''
# #         return (self.a ** 2 * self.h) / (4 * 3 ** .5)

# #     def get_S(self):
# #         '''метод вычисления площади'''
# #         return (self.a ** 2 * 3 ** .5) / 4 + ((3 * self.a) / 2) * (self.h ** 2 + self.a ** 2 / 12) ** .5

# #     def get_answer(self):
# #         if not self.correct: return ['error']
# #         return map(lambda x: round(x, 3), (self.get_V(), self.get_S()))

# # # создание объекта через распакованный массив (список)
# # p = Pyramid(*(float(input()) for _ in 'ab'))
# # print(*p.get_answer())


# x_a = float(input())
# y_a = float(input())

# x_b = float(input())
# y_b = float(input())

# x_c = float(input())
# y_c = float(input())

# from math import sqrt

# def compute_len(x_0, y_0, x_1, y_1):

#     len_line = sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)

#     return len_line


# def compute_area(a_1, a_2, a_3):
#     p = (a_1 + a_2 + a_3) / 2
#     area = sqrt(p * (p - a_1) * (p - a_2) * (p - a_3))
#     return area

# def radius_in_circle(a, b, c):
#     half_p = (a + b + c) / 2
#     up_part = (half_p - a) * (half_p - b) * (half_p - c)
#     return sqrt(up_part / half_p)

# def radius_out_circle(a, b, c):
#     s = compute_area(a, b, c)
#     return (a * b * c) / (4 * s)

# def sum_medians_len(a, b, c):
#     m_a = 0.5 * sqrt(2 * (c ** 2 + b ** 2) - a ** 2)
#     m_b = 0.5 * sqrt(2 * (c ** 2 + a ** 2) - b ** 2)
#     m_c = 0.5 * sqrt(2 * (a ** 2 + b ** 2) - c ** 2)
#     return m_a + m_b + m_c

# a = compute_len(x_a, y_a, x_b, y_b)
# b = compute_len(x_b, y_b, x_c, y_c)
# c = compute_len(x_a, y_a, x_c, y_c)

# if a + b <= c or b + c <= a or a +c <= b:
#     print("error")
# else:
#     print(round(radius_in_circle(a, b, c), 4),round(radius_out_circle(a, b, c), 4), round(sum_medians_len(a, b, c), 4))

# '''
# радиус вписанной в треугольник окружности;
# радиус описанной вокруг треугольника окружности;
# сумму длин трех медиан треугольника.
# '''


# from math import sqrt, acos, degrees

# def compute_len(x_0,y_0,x_1,y_1):

#     len_line = sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)

#     return len_line

# def compute_area(a_1, a_2, a_3):

#     p = (a_1 + a_2 + a_3) / 2

#     area = sqrt(p * (p - a_1) * (p - a_2) * (p - a_3))

# def compute_angle(a_1, a_2, a_3):

#     angle_rad = acos((a_1 ** 2 + a_2 ** 2 - a_3 ** 2)/
#                      (2 * a_1 * a_2))

#     return degrees(angle_rad)

# # x_a = 0; y_a = 10; x_b =-5; y_b = 0; x_c = 5; y_c = 0
# # x_a = 0; y_a = 1; x_b =0; y_b = 0; x_c = 1; y_c = 0
# # x_a = 0; y_a = 0; x_b =1; y_b = 1; x_c = 2; y_c = 2
# x_a = 12; y_a = -5; x_b = 5; y_b = -1; x_c = 6; y_c = 8
# # x_a = 0; y_a = 7; x_b = 2.6; y_b = -9.1; x_c = 3.5; y_c = 1


# a_1 = round(compute_len(x_a, y_a, x_b, y_b), 3)
# b_1 = round(compute_len(x_b, y_b, x_c, y_c), 3)
# c_1 = round(compute_len(x_a, y_a, x_c, y_c), 3)

# print(a_1, b_1, c_1)


# # https://stepik.org/lesson/264349/step/15?unit=245268
# # разобраться чего хотели в этой задаче, перечитать условие с коментариями
# '''
# удалить ввод имени и приветствие;
# удалить подсказки из операторов input;
# исправить оператор вывода результатов;
# проверить, чтобы все строки в кавычках не заканчивались пробелами.
# '''

# age = int(input())
# height = float(input())
# weight = float(input())

# if age < 10 or height <= 0 or height > 3 or weight <= 0 or weight > 500:
#     print("Ошибочные входные данные")
# else:
#     bmi = weight / height ** 2
#     bmi = round(bmi, 2)

#     if age < 45:
#         if 18.5 > bmi:
#             description = "недостаточной массой тела."
#         elif 18.5 <= bmi <= 24.99:
#             description = "нормальной массой тела."
#         elif 25 <= bmi <= 29.99:
#             description = "избыточной массой тела."
#         else:
#             description = "ожирением."
#     else:
#         if 22 > bmi:
#             description = "недостаточной массой тела."
#         elif 22 <= bmi <= 26.99:
#             description = "нормальной массой тела."
#         elif 27 <= bmi <= 31.99:
#             description = "избыточной массой тела."
#         else:
#             description = "ожирением."
#     print("bmi=", bmi, "Вы относитесь к группе людей с", description)
