
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

