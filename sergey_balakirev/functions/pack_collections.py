
# Подвиг 2. Вводится список из семи целых чисел в одну строчку через пробел. 
# Необходимо первые четыре числа занести в переменную lst, а остальные три в отдельные переменные x, y, z. 
# Сделать с использованием оператора упаковки. Вывести список lst на экран с помощью команды: print(*lst)

# 56 4 -23 2 0 3 5
# *lst, x, y, z = list(map(int, input().split()))
# print(*lst)


# Подвиг 3. Вводятся названия городов в одну строчку через пробел. На основе этой строки необходимо сформировать список 
# из названий. А, затем, используя оператор распаковки *, преобразовать этот список в кортеж lst_c. 
# Результат вывести на экран командой: print(lst_c)
# in_lst = input().split()
# lst_c = (*in_lst, )
# print(lst_c)


# Подвиг 4. Вводятся два целых значения a и b (a < b) в одну строчку через пробел. Необходимо сформировать список из 
# целых чисел от a до b (включительно) с шагом изменения 1, используя функцию range, оператор [] 
# и оператор распаковки *. Вывести полученный список на экран командой: print(*lst)
# start, finish = map(int, input().split())
# print(*[value for value in range(start, finish + 1)])


# Подвиг 5. Вводится список вещественных чисел и список названий городов, каждый в отдельной строке. 
# Необходимо сформировать единый список lst, в котором сначала идут числа, а затем, названия городов. 
# Реализовать программу с помощью оператор распаковки *. Вывести полученный список на экран командой: print(*lst)

# lst =  *list(map(float, input().split())), *input().split()
# print(*lst)


# Подвиг 6. Имеется словарь, содержащий пункты меню:
# menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
# Дополнительно вводятся еще пункты меню в виде строк в формате:
# название_1=url_1
# название_N=url_N
# Необходимо эту введенную информацию преобразовать в словарь и добавить к словарю menu, используя оператор распаковки 
# для словарей. На результирующий словарь должна вести переменная menu. Выводить словарь не нужно, только сформировать.
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
lst_in = ['Города=about-cities', 'Машины=read-of-cars', 'Самолеты=airplanes']
t_dict = dict(i.split('=') for i in lst_in)
menu =  {**menu, **t_dict}
