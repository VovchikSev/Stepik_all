"""doc."""
# 4  Цикл while
# 4.1 Знакомство с циклом while


# """
# Напишите программу, которая проверяет, является ли введённое натуральное число степенью двойки. 
# Если да, то выводится сама эта степень; если нет, выводится «НЕТ»
# """
# n = int(input())
# b = 1
# a = 0
# while b < n:
#     b = b * 2
#     a += 1

# if b == n:
#     print(a)
# else:
#     print('НЕТ')

# непрерывный ввод
# val = input()
# my_list = [val]
#
# while True:
#     t = input()
#     if 4 < len(t) < 10:
#         my_list.append(t)
#     else:
#         break
#
# print(my_list[-1])

# all_tasks, minutes = map(int, input().split())
# last_time = 4 * 60 - minutes
# r_tasks = 0
# while all_tasks > 0:
#     time_for_task = (r_tasks + 1) * 5
#     if last_time - time_for_task >= 0:
#         last_time -= time_for_task
#         r_tasks += 1
#         all_tasks -= 1
#     else:
#         break
# print(r_tasks)
# print(last_time)

# all_items = int(input())
# used_items = a = 1
# count = 0
# while all_items - used_items >= 0:
#     count += 1
#     all_items -= used_items
#     a += 1
#     used_items += a
# print(count)

# first_len, second_len = map(int, input().split())
# first_list = list(map(int, input().split()))
# second_list = list(map(int, input().split()))
# first_pointer = second_pointer = 0
# result_list = []
# while first_pointer < first_len and second_pointer < second_len:
#     if first_list[first_pointer] < second_list[second_pointer]:
#         result_list.append(first_list[first_pointer])
#         first_pointer += 1
#     else:
#         result_list.append(second_list[second_pointer])
#         second_pointer += 1
# if first_pointer < first_len:
#     result_list += first_list[first_pointer:]
# if second_pointer < second_len:
#     result_list += second_list[second_pointer:]
# print(*result_list)


# man_len = int(input())
# man_list = sorted(list(map(int, input().split())))
# woman_len = int(input())
# woman_list = sorted(list(map(int, input().split())))
# man_pointer = woman_pointer = count_couples = 0
#
# while man_pointer < man_len and woman_pointer < woman_len:
#     if abs(man_list[man_pointer] - woman_list[woman_pointer]) < 2:
#         count_couples += 1
#         woman_pointer += 1
#         man_pointer += 1
#     else:
#         if man_list[man_pointer] < woman_list[woman_pointer]:
#             man_pointer += 1
#         else:
#             woman_pointer += 1
# print(count_couples)


# 4.3 Обход всех цифр числа с помощью while

# Обход всех цифр чис
# number = int(input())
# while number > 0:
#     current_number = number % 10
#     number = number // 10


# перевод числа в другую систему исчисления (foundation) результат в обратном порядке
# number = int(input())
# foundation = 2
# while number > 0:
#     print(number % foundation)
#     number //= foundation

# 4.4 Нахождение всех делителей числа


# number = int(input())
# is_index = lambda x, y: x * x < y
# index = 1
# list_result = []
# # while (index * index) <= number:
# для суммы всех делителей важно обработать единицу как входное число
# while is_index(index, number) or index == number:
#     if number % index == 0:
#         list_result.append(index)
#         if index != number // index:
#             list_result.append(number // index)
#     index += 1
# # print(list_result)
# print(sum(list_result))

# Простое число. 1 не простое число
# number = int(input())
# is_index = lambda x, y: x * x < y
# index = 1
# list_result = []
# while number > 1 and is_index(index, number) and len(list_result) < 3:
#     if number % index == 0:
#         list_result.append(index)
#         if index != number // index:
#             list_result.append(number // index)
#     index += 1
# print("Yes" if len(list_result) == 2 else "No")


# 4.5 Алгоритм Евклида
# НОД по алгоритму Евклида
# a, b = 21, 35
# while a != b:
#     if a > b:
#         a -= b
#     else:
#         b -= a
# долгий алгоритм
#  теоретическая  a * b = НОД * НОК
# НОК = (a * b) / НОД
# a, b = int(input()), int(input())
# while b > 0:
#     b, a = a % b, b
# print(a)


# поиск НОК через функцию НОД
# def nod(first: int, second: int) -> int:
#     while second > 0:
#         second, first = first % second, second
#     return first
#
#
# a, b = map(int, input().split())
# print(nod(a, b), a * b // nod(a, b))

# 4.6 Инструкции break, continue, else


my_str = input()
index = 0
while index <= len(my_str) - 1:
    if my_str[index] == 'a' or my_str[index] == 'e':
        print("Ага! Нашлась")
        break
    else:
        print(f"Текущая буква: {my_str[index]}")
    index += 1
else:
    print("Распечатали все буквы")
