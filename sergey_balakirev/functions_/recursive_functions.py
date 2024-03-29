
# Подвиг 2. Вводится целое положительное число N. Необходимо написать рекурсивную функцию с именем get_rec_N,
# которая отображает на экране последовательность целых чисел от 1 до N (включительно).
# Каждое число выводится с новой строки. В качестве параметра функция get_rec_N должна принимать одно числовое значение.
#  То есть, иметь только один параметр. Начальный вызов функции будет выглядеть так: get_rec_N(N)
# def get_rec_N(in_value:int):
#     if in_value > 1:
#         get_rec_N(in_value - 1)
#     print(in_value)


# Подвиг 3. Вводится список целых чисел в одну строчку через пробел. Необходимо вычислить сумму этих введенных значений,
# используя рекурсивную функцию (для перебора элементов списка) с именем get_rec_sum. Функция должна возвращать
# значение суммы. (Выводить на экран она ничего не должна).
# Вызовите эту функцию и выведите вычисленное значение суммы на экран.
# 8 11 -5 4 3

# def get_rec_sum(in_lst):
#     if not in_lst:
#         return 0
#     else:
#         return in_lst[0] + get_rec_sum(in_lst[1:])


# in_lst = list(map(int, input().split()))
# print(get_rec_sum(in_lst))


# Подвиг 4. Вводится натуральное число N. Необходимо с помощью рекурсивной функции fib_rec(N, f=[])
# (здесь N - общее количество чисел Фибоначчи; f - начальный список этих чисел) сформировать последовательность
# чисел Фибоначчи по правилу: первые два числа равны 1 и 1, а каждое следующе значение равно сумме двух предыдущих.
# Пример такой последовательности для первых 7 чисел: 1, 1, 2, 3, 5, 8, 13, ...
# N = int(input())
# def fib_rec(N, f=[]):
#     if not f:
#         f.append(1)
#         f.append(1)
#     else:
#         f.append(f[-2] + f[-1])
#     if len(f) < N:
#         fib_rec(N, f)
#     return f

# print(fib_rec(N))


# Подвиг 5. Вводится целое неотрицательное число n. Необходимо с помощью рекурсивной функции fact_rec вычислить факториал
# числа n. Напомню, что факториал числа, равен: n! = 1 * 2 * 3 *...* n. Функция должна возвращать вычисленное значение.
# Вызывать функцию не нужно, только объявить со следующей сигнатурой: def fact_rec(n):

# def fact_rec(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact_rec(n - 1)

# print(fact_rec(int(input())))


# Подвиг 6. Имеется следующий многомерный список:
from turtle import left, right


d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
# С помощью рекурсивной функции get_line_list создать на его основе одномерный список из значений элементов списка d.
# Функция должна возвращать новый созданный одномерный список.  (Только возвращать, выводить на экран ничего не нужно.)
# Вызывать функцию не нужно, только объявить со следующей сигнатурой:def get_line_list(d,a=[]):
# где d - исходный список; a - новый формируемый.

# def get_line_list(d, a=[]):
#     for lst_value in d:
#         if isinstance(lst_value, list):
#             get_line_list(lst_value, a)
#         else:
#             a.append(lst_value)

#     return a

# print(get_line_list(d))


# Подвиг 7. Лягушка прыгает вперед и может скакнуть либо на одно деление, либо сразу на два.
# Наша задача определить количество вариантов маршрутов, которыми лягушка может достичь риски под номером N
# (натуральное число N вводится с клавиатуры).
# Решать задачу следует с применением рекурсивной функции. Назовем ее get_path. Алгоритм решения будет следующий.
# Рассмотрим, например, риску под номером 4. Очевидно, в нее лягушка может скакнуть либо с риски номер 2,
# либо с риски номер 3. Значит, общее число вариантов перемещений лягушки можно определить как:
# get_path(4) = get_path(3) + get_path(2)
# Аналогично будет справедливо и для любой риски N:
# get_path(N) = get_path(N-1) + get_path(N-2)
# А начальные условия задачи, следующие:
# get_path(1) = 1
# get_path(2) = 2
# Реализуйте такую рекурсивную функцию, которая должна возвращать количество вариантов перемещений лягушки для риски
# под номером N.
# Вызовите эту функцию для введенного числа N и отобразите результат на экран

# def get_path(N):
#     if N in (1,2):
#         return N
#     return get_path(N-1) + get_path(N-2)


# jamps = int(input())
# print(get_path(jamps))


# Великий подвиг 8. Вводится список из целых чисел в одну строчку через пробел. Необходимо выполнить его сортировку
# по возрастанию с помощью алгоритма сортировки слиянием. Функция должна возвращать новый отсортированный список.
# Вызовите результирующую функцию сортировки для введенного списка и отобразите результат на экран в виде
# последовательности чисел, записанных через пробел.
# 8 11 -6 3 0 1 1

# def merge_sort(num_lst: list):# -> list:
#     """_summary_
#     Сортирует введенный список чисел
#     Args:
#         num_lst (list): список чисел
#         теоретически может быть любой сравнимый тип, но тогда поведение не гарантируется
#         для данной задачи не подходит, требуется сгенерировать новый возвращаемый список после сортировки 
#         и рекурсию поддержать
#     """
#     if len(num_lst) > 1:
#         mid = len( num_lst)
#         left_lst = num_lst[:mid]
#         right_lst = num_lst[mid:]
#         merge_sort(left)
#         merge_sort(right)

#     left_index = right_index = result_index = 0

#     while left_index < len(left_lst) and right_index < len(right_lst):
#         if left_lst[left_index] < right_lst[right_index]:
#             num_lst[result_index] = left_lst[left_index]
#             left_index += 1
#         else:
#             num_lst[result_index] = right_lst[right_index]
#             right_index += 1
#             result_index += 1

#     while left_index < len(left_lst):
#         num_lst[result_index] = left_lst[left_index]
#         left_index += 1
#         result_index += 1
#     while right_index < len(right_lst):
#         num_lst[result_index]

def merge_sort(num_lst:list)->list:
    if len(num_lst) < 2:
        return num_lst
    result = []          
    mid = int(len(num_lst) / 2)
    left_list = merge_sort(num_lst[:mid])
    right_list = merge_sort(num_lst[mid:])
    while (len(left_list) > 0) and (len(right_list) > 0):
        if left_list[0] > right_list[0]:
            result.append(right_list[0])
            right_list.pop(0)
        else:
            result.append(left_list[0])
            left_list.pop(0)
    result += left_list
    result += right_list
    return result

in_lst = [int(value) for value in input().split()]    

print(merge_sort(in_lst))
print(in_lst)
