# import numpy as np
# решено и сдано!
# def get_trend(x, a, pow:int)->float:
#     if pow == 1:
#         y =  a[0]* x + a[1]
#     elif pow == 2:
#         y = a[0] * x **2 + a[1]* x + a[2]
#     elif pow == 3:           
#         y = a[0] * x ** 3 + a[1] * x ** 2 + a[2] * x + a[3]
#     return y

# # альтернативная функция, по полиндрому формируется массив необходимой длинны. 
# # исходя из этого и генерируется значение
# # def get_trend(x, a):
# #     n = len(a)
# #     y = 0
# #     for i in range(n):
# #         y += a[i] * x **(n-i-1)
# #     return y
# counry = input()
# tourists = np.array(input().split(), dtype=float)
# pow_polynom = int(input())
# project_2018 = float(input())
# year_list = np.array(range(2005, 2018), dtype=int) # массив через numpy np.arange(2005, 2018)

# my_trend = np.polyfit(year_list, tourists, pow_polynom) # это лишняя строка, значение можно вставить непосредственно в вызов
# tourists_2018 = get_trend(2018, my_trend, pow=pow_polynom)

# err = abs((project_2018 - tourists_2018) / project_2018) * 100

# print(f"Страна:{counry:>6s}, прогноз:{tourists_2018:6.3f}млн чел, относительная погрешность:{err:4.2f}проц." )


# '''
# https://stepik.org/lesson/270175/step/5?unit=251215

# Sample Input 1:
# 167 # H - Высота колеса, целое число
# 30  # T - Время полного оборота в минутах, (целое число);
# 15  # t - Время в минутах (вещественное число).

# Sample Output 1:
# Высота = 167.00 м
# # "Высота = %6.2f м"
# Решение примерное, не забыть проверку корректных данных
# T > 0 
# t <= T

# h=H/2*(1-cos(2*pi*t/T)), 0<=t<=T
# или через синус
# h = H * (sin((2 * t * pi / T) - pi / 2) + 1) / 2
# '''
# from math import sin, pi, cos
# H = int(input())
# T = int(input())
# t = float(input())

# if T > 0 and (t <= T or t == 0):
#     h = H * (sin((2 * t * pi / T) - pi / 2) + 1) / 2
#     print(f'Высота = {h:6.2f} м')
#     h = H/2 * (1-cos(2*pi*t/T)) # , 0<=t<=T
#     print(f'Высота = {h:6.2f} м')
# else:
#     print("error")    


# '''
# https://stepik.org/lesson/270175/step/4?unit=251215
# Даны длины стороны основания и высоты нескольких пирамид. 
# Вывести номера пирамид, имеющих максимальный объем, и номера пирамид, имеющих минимальную площадь боковой поверхности.
# Входные данные:
# строка, в которой через пробел перечислены длины оснований (вещественные числа);
# строка, в которой через пробел перечислены высоты пирамид (вещественные числа).
# Выходные данные:
# номер пирамиды (нумерация начинается с 0), имеющей максимальный объем, и значение объема;
# номер пирамиды (нумерация начинается с 0), имеющей минимальную площадь боковой поверхности, и значение площади.
# Sample Input:
# 144 189 230 219 215 
# 94 105 146.6 105 144
# Sample Output:
# Vmax:  2, 2585046.67, Smin:  0, 34100.95

# Для основания a и высоты h:
# объём пирамиды = (a * a * h) / 3
# площадь боковой поверхности = 2 * a * hypot(a / 2, h)
# '''
# from math import hypot

# len_array = list(map(int, input().split()))
# height_array = list(map(float, input().split()))
# v = []
# s_p = []
# for index in range(len(len_array)):
#     v.append((len_array[index] ** 2 * height_array[index]) / 3)
#     s_p.append(2 * len_array[index] * hypot(len_array[index] / 2, height_array[index]))
#     # s_p.append(2 * len_array[index] * hypot[len_array[index] / 2, height_array[index]])
# index_v_max = v.index(max(v))    
# index_s_min =s_p.index(min(s_p))
# print(f"Vmax: {index_v_max:2d}, {v[index_v_max]:8.2f}, Smin: {index_s_min:2d}, {s_p[index_s_min]:8.2f}")   


# '''
# https://stepik.org/lesson/270175/step/3?unit=251215
# Интервал (шт/км)	Оплата (S$)
# <=30	                1
# от 31 до 60	       1.5
# 61 до 120	            3
# >120	               4.5
# Sample Input 1:
# 5 2 2 4 3 4 4
# 432 202 40 124 106 104 76

# Sample Output 1:
# Длина пути:  24 км, оплата: 12.00 S$
# '''
# total_pay = 0
# patch_array = list(map(int, input().split()))
# auto_amount = list(map(int, input().split()))
# for index in range( len(patch_array)):
#     value = auto_amount[index] / patch_array[index]
#     if value <= 30:
#         total_pay += 1
#     elif 30 < value <= 60:
#         total_pay += 1.5
#     elif 60 < value <= 120:
#         total_pay += 3
#     elif value > 120:
#         total_pay += 4.5
# print(f"Длина пути: {sum(patch_array):3d} км, оплата: {total_pay:5.2f} S$")             
# # разобрать способ решения этой же задачи
# import numpy as np
# path = np.array(input().split(), dtype=int)
# auto = np.array(input().split(), dtype=int)
# price = (1, 1.5, 3, 4.5)
# calc = np.array([30, 60, 120])
# full = sum(price[sum(v > calc)] for v in auto / path)
# print(f'Длина пути: {path.sum():3d} км, оплата: {full:5.2f} S$')


# '''
# https://stepik.org/lesson/270175/step/2?unit=251215
# Написать программу, которая выводит номера всех велосипедов, которые открыты более 12 часов.
# Входные данные:
# строка, состоящая из значений, разделенных пробелами. Каждое значение либо 0, если велосипедом не пользуются, 
# либо количество минут, прошедших с момента открытия замка. 
# Номер значения времени в списке соответствует номеру велосипеда, нумерация начинается с 0.
# Выходные данные:
# номера велосипедов, которые открыты больше 12 часов, каждый номер вывести на отдельной строке.
# '''
# arenda_list = list(map(int, input().split()))
# for index in range(len(arenda_list)):
#     if arenda_list[index] > 12 * 60:
#         print(index) 


# '''
# Готовое решение https://stepik.org/lesson/270175/step/1?unit=251215
# Билет на самолет на одного человека стоит k рублей туда и обратно. Автомобиль расходует 12 литров бензина на 100 км, 
# а цена бензина –  p рублей за 1 литр. Расстояние от города А до В -  s км. 
# Сколько рублей придется заплатить за самую дешевую поездку на троих туда и обратно?
# На входе:
# стоимость билета на самолет (вещественное число); k (умножать на три нужно)
# цена бензина (вещественное число); p цена за литр. Высчитать стоимость отно
# расстояние от города А до города В (вещественное число). S киллометров

# сумма самой дешевой поездки (вещественное число) или '"error", если введены ошибочные данные.
# Результат округлить до двух знаков после запятой (использовать функцию round()).
# '''
# # ввод данных
# aero_ticket = float(input()) 
# one_liter_cost = float(input())
# distance = float(input())
# if aero_ticket <= 0 or one_liter_cost <= 0 or distance <= 0:
#     print("error")
# else:
#     aero_cost = aero_ticket * 3
#     auto_cost = distance * 2 / 100 * 12 * one_liter_cost    
#     print(round(auto_cost, 2) if auto_cost < aero_cost else round(aero_cost, 2))


# import numpy as np 
# # https://stepik.org/lesson/269788/step/3?unit=250835
# list_angle = np.array(input().split(), dtype=int)
# list_distance = np.array(input().split(), dtype=float)
# my_angle = int(input())

# def get_trend(x, a):
#     y = a[0] * x **2 + a[1]* x + a[2]
#     return y
# '''
# 27 34 41 48 55 62 69 76 83 90 97
# 75.23 95.49 98.03 89.5 84.57 82.07 69.58 48.82 26.36 0.0 -26.12
# 34
# Дальность:  89.19 м
# "Дальность: %6.2f м"
# '''

# trend_len = 0
# my_trend = np.polyfit(list_angle, list_distance, 2)
# point_trend = get_trend(my_angle, my_trend)
# print(f"Дальность: {point_trend:6.2f} м")


# https://stepik.org/lesson/269788/step/2?unit=250835
# import numpy as np 
# r_om = np.array(input().split(), dtype=float)
# i_amp = np.array(input().split(), dtype=float)
# r = 1 / np.sum(1 / r_om)
# i = np.sum(i_amp)
# print(f"R = {r:6.3f} Ом, I = {i:6.3f} А, U = {i * r:6.3f} В")



# import numpy as np 
# from math import sqrt
# '''
# Создать массив точек points.
# Найти координаты "средней" точки (среднее значение каждой координаты массива точек) - это центр круга.
# Сформировать массив расстояний от средней точки до каждой точки массива points, 
# используя формулу расстояния между двумя точками); (points_dst)
# Найти максимальное расстояние - это радиус круга.
# '''

# def points_dst(x_0:float, y_0:float, x_1:float, y_1:float):
#     return sqrt((x_0 - x_1) ** 2 + (y_0 - y_1) ** 2)

# start_vectors = []
# for _ in range(int(input())):
#     start_vectors.append(input().split())    

# points = np.array(start_vectors, dtype=float)
# avg_point = np.mean(points, 0)
# r_array = []
# for point in points:
#     r_array.append(points_dst(avg_point[0], avg_point[1], point[0], point[1]))

# print(f"центр в точке ({avg_point[0]:6.3f}, {avg_point[1]:6.3f}), r = {max(r_array):6.3f}")



# import numpy as np
# import math 

# start_vectors = []
# for _ in range(int(input())):
#     start_vectors.append(input().split())    
# ver = np.array(start_vectors, dtype=int)
# grad = int(input())    

# res_vextor = rotate = np.array([[math.cos(math.radians(grad)), math.sin(math.radians(grad))],[-math.sin(math.radians(grad)), math.cos(math.radians(grad))]])

# koord = np.dot(ver, rotate)
# avg = np.mean(koord, 0)

# print("avg_x = %6.2f, avg_y = %6.2f" % (np.round(avg[0], 2), np.round(avg[1], 2)))

# # готовое решение на задачу https://stepik.org/lesson/269787/step/7?unit=250834
# import numpy as np
# import numpy.linalg as alg

# a_matrix = np.array([[-2, -8.5, -3.4, 3.5], [0, 2.4, 0, 8.2], [2.5, 1.6, 2.1, 3], [0.3, 0.4, -4.8, 4.6]])
# b_matrix = np.array([-1.8, -3.28, -0.5, -2.83])

# a_inv = alg.inv(a_matrix)
# x_matrix = np.dot(alg.inv(a_matrix) , b_matrix)
# print(np.round(x_matrix,1))


 # import numpy as np
# import numpy.linalg as alg
# # Создать матрицу A в виде двухмерного массива, вывести ее на экран 
# # («\n» используется для перехода на следующую строку при выводе):
# a = np.array([[3, 4, -2], [-2, -1, 4], [1, 2, 1]])
# print("A :\n", a)

# # Создать матрицу B , вывести ее на экран :
# b = np.array([[1, -3, -2, 1], [2, 4, -2, -1], [5, -2, 0, -2]])
# print("B :\n", b)

# # Вычислить произведение A и B, вывести результат:
# c = np.dot(a, b)
# print("A*B:\n", c)

# # Вычислить определитель матрицы A, вывести результат:
# det_a = alg.det(a)
# print("dеt(A): ", round(det_a, 1))

# # Вычислить обратную матрицу A**(-1):
# a_inv = alg.inv(a)
# print("A^-1:\n", np.round(a_inv,1))

# # Вычислить матричное выражение  det(A) * A**(-1)  * B - 10 * A**3 для упрощения А**3 вычислим отдельно:
# a_3 = np.dot(a, np.dot(a,a))
# result = det_a * np.dot(a_inv, b) - 10 * np.dot(a_3, b)
# print("Result:\n", result)

# import numpy as np
# def get_trend2(x, a):
#     y = a[0] * x **2 + a[1]* x + a[2]
#     return y
    
# def get_trend(x, a):
#     y = a[0] * x + a[1]
#     return y

# x_array = np.array(input().split(), dtype=float)
# y_array = np.array(input().split(), dtype=float)

# trend_1 = np.polyfit(x_array, y_array, 1)
# trend_2 = np.polyfit(x_array, y_array, 2)
# delta_1 = np.abs((y_array - get_trend(x_array, trend_1)) / y_array) * 100
# delta_2 = np.abs((y_array - get_trend2(x_array, trend_2)) / y_array) * 100
# avg_error1 = np.average(delta_1)
# avg_error2 = np.average(delta_2)

# if avg_error1 <= avg_error2:
#     # print("%5.3f %5.3f" % (trend_1))
#     print(f"{trend_1[0]:5.3f} {trend_1[1]:5.3f}")
# else:
#     print(f"{trend_2[0]:5.3f} {trend_2[1]:5.3f} {trend_2[2]:5.3f}")
    

# print(avg_error1, avg_error2)


# import matplotlib.pyplot as plt
# import numpy as np
# def get_trend(x, a):
#     y = a[0] * x **2 + a[1]* x + a[2]
#     return y
# # Создадим списки, необходимые для построения линии тренда:
# x_array = np.array([18.6, 99.9, 157.2, 219.9, 303.7, 399.6, 452.5, 528.4, 613.8, 669.7, 750.6, 816.2, 906.2])
# h_array = np.array([85.7, 173.8, 196.7, 259.6, 332.5, 379.3, 414.2, 419.7, 461.3, 438.9, 447.8, 434.1, 441.4])
# a = np.polyfit(x_array, h_array, 2)
# # список со значениями координат по оси OX - целые числа от 0 до 1500 (так как наша мишень находится в точке x = 1450), 
# # с шагом 10 :
# x_trend = [i for i in range(0,1500,10)]
# # список координат по оси OY, значения которого посчитаны с помощью функции тренда
# y_trend = [get_trend(x, a) for x in x_trend]
# # Сформируем линию для отображения точных координат положений снаряда: 

# plt.plot(x_array, h_array, 'go', label="положение снаряда")
# # Сформируем график линии тренда:
# plt.plot(x_trend, y_trend, 'r-', label="линия тренда")
# # Отформатируем оси, выведем легенду и покажем область построения:
# plt.gca().spines["left"].set_position("zero")
# plt.gca().spines["bottom"].set_position("zero")
# plt.gca().spines["top"].set_visible(False)
# plt.gca().spines["right"].set_visible(False)

# x_target = 1450
# h_target = get_trend(x_target, a)

# # plt.plot(x_target, h_target, 'b+', markersize=12)
# plt.plot([x_target], [h_target], 'b+', markersize=12)

# plt.legend(loc="lower center")
# plt.show()

# import numpy as np
# https://stepik.org/lesson/269786/step/4?unit=250833
# #  Сформируем массивы координат движения снаряда:

# # x_array = np.array([18.6, 99.9, 157.2, 219.9, 303.7, 399.6, 452.5, 528.4, 613.8, 669.7, 750.6, 816.2, 906.2])
# # h_array = np.array([85.7, 173.8, 196.7, 259.6, 332.5, 379.3, 414.2, 419.7, 461.3, 438.9, 447.8, 434.1, 441.4])

# x_array = np.array(input().split(), dtype=float)
# h_array = np.array(input().split(), dtype=float)
# #  Построим траекторию движения снаряда, используя в качестве линии тренда полином второй степени. 
# # Найдем его коэффициенты:

# a = np.polyfit(x_array, h_array, 2)
# #  Создадим функцию для вычисления значений полинома второй степени в точке x, разместим ее в начале программы,
# #  после импорта модуля:

# def get_trend(x, a):
#     y = a[0] * x **2 + a[1]* x + a[2]
#     return y

# # С помощью полученного тренда вычислим высоту, на которой находилась пушка. Значение координаты по оси ОХ 
# # в этой точке равно 0.
# h_zero = get_trend(0, a)
# # print("Высота, на которой стоит пушка: %6.2f м" % h_zero)

# #  Вычислим, на какой высоте будет находиться снаряд в точке по оси ОХ, где расположена мишень
# x_target = float(input()) #1450
# h_target = get_trend(x_target, a)
# # print("Высота, в точке %4d м: %6.2f м" % (x_target, h_target))

# #  Определим, попадет ли снаряд в цель, если известно что мишень расположена на высоте 51 метр, учитывая, 
# # что радиус мишени 50 см =0.5 м. Для этого найдем модуль разности между высотой, на которой расположена мишень, 
# # и положением снаряда, вычисленного с помощью линии тренда. Затем сравним полученное значение с радиусом мишени 
# # и выведем результат.
# # delta_h = abs(51 - h_target)
# # delta_h = abs(float(input()) - h_target)
# delta_h =  abs(float(input()) - h_target)
# print(f"h0 = {h_zero:6.2f}, {'yes' if delta_h <= 0.5 else 'no'}")
# # if delta_h <= 0.5:
# #     print("Снаряд попадет в мишень.")
# # else:
# #     print("Снаряд не попадет в мишень.")


# from tracemalloc import start
# import numpy as np
# path = np.array(input().split(), dtype=int)
# speed = np.array(input().split(), dtype=int)
# start, finish = int(input()), int(input()) + 1
# path = path[start:finish]
# speed = speed[start:finish]

# len_path = path.sum()
# time = path / speed
# sum_time = time.sum()
# avg_speed = len_path / sum_time
# print(f"S = {len_path:3d} км, T = {sum_time:5.2f} час, V = {avg_speed:5.2f} км/ч")


# import numpy as np
# costs = np.array([1200, 1300, 900, 1450, 1300, 1000, 900, 1000, 1450, 1450, 1300, 1400])
# # посчитать сумму за проезд в зимние месяцы
# sum_winter = costs[0] + costs[1] + costs[11]  # вставить выражение так лучше: sum(costs[0:2]) + costs[11]
# # посчитать сумму за проезд в летние месяцы
# sum_summer = costs[5] + costs[6] + costs[7] #вставить выражение так лучше: sum(costs[5:8])
# if sum_winter > sum_summer:
#     print("Зимой на проезд потрачено больше денег, сумма: %4d руб." % sum_winter)
# elif sum_winter < sum_summer:
#     print("Летом на проезд потрачено больше денег, сумма: %4d руб." % sum_summer)
# else:
#     print("Зимой и летом на проезд тратится одинаковая, сумма: %4d руб." % sum_winter)
# # найти максимальную сумму оплаты за месяц  
# max_costs = costs.max() # вставить выражение
# # найти номера месяцев, в которые тратилась наибольшая сумма
# max_month = np.where(costs == max_costs)[0] # вставить выражение
# print(f"Самая большая сумма:{max_costs:4d} руб., потрачена в следующих месяцах:", max_month + 1)
# # print("Самая большая сумма:%4d руб., потрачена в следующих месяцах:" % max_costs, max_month + 1)


# import numpy as np
# path = np.array(input().split(), dtype=int)
# speed = np.array(input().split(), dtype=int)
# len_path = path.sum()
# time = path / speed
# time_path = time.sum()
# print(f"S = {len_path:3d} км, T = {time_path:5.2f} час, V = {len_path / time_path:5.2f} км/ч")
# '''
# 14 11 11 19 7 18 9 10 13
# 42 50 30 43 39 36 53 60 49
# '''
# # импортировать модуль numpy. Под псевдонимом np
# import numpy as np
# # Сформируем массивы длин участков и скорости автомобиля на них:
# path = np.array([15, 5, 12, 2, 21, 17, 21, 3, 10, 5]) 
# '''участки пути от А до B условных единиц'''
# speed = np.array([60, 30, 60,45, 50, 60, 50, 40, 60, 40])
# '''скорости на участках path'''

# # Вычислим длину пути от А до В и выведем результат:
# len_path = path.sum()
# print("Расстояние между пунктами А и В :", len_path)
# # Расстояние можно было вычислить и другим способом:
# # Результат получится совершенно одинаковым.
# # len_path = np.sum(path)
# # print("Расстояние между пунктами А и В :", len_path)

# # Вычислим время прохождения автомобилем каждого участка, результат получится в виде массива, 
# # каждый элемент массива при выводе округлим до 2-х знаков после запятой:
# time = path / speed
# print("Время на каждом участке :", np.round(time, 2))

# # Вычислим общее время в пути,  при выводе округлим значения:
# sum_time = time.sum()
# print("Общее время в пути : ", round(sum_time, 2))

# # Посчитаем среднюю скорость автомобиля (среднюю путевую скорость):
# avg_speed = len_path / sum_time
# print("Средняя скорость : ", round(avg_speed, 2))
# # Среднюю скорость нельзя вычислять как среднее значение скорости на всех участках!