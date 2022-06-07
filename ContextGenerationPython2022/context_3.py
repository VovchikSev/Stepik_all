
# Реализуйте функцию index_of_nearest(), которая принимает на вход список целых чисел и искомое число.
# Задача функции — найти в списке ближайшее число к искомому и вернуть его индекс.
# Примечание 1. Если переданный в функцию список пуст, то функция должна вернуть значение -1
# Примечание 2. Если в списке содержится несколько чисел, одновременно являющихся ближайшими
# к искомому числу, то возвращается наименьший из индексов ближайших чисел.

# def index_of_nearest(in_list: list, number: int) -> int:
#     ret_index = -1
#     for index in range(len(in_list)):
#         if ret_index < 0:
#             ret_index = index
#         if abs(number - in_list[ret_index]) > abs(number - in_list[index]):
#             ret_index = index
#     return ret_index
#     # if not len(in_list):
#     #     return -1
#     # ret_value = in_list[0]
#     # for index in range(1, len(in_list) - 1):
#     #     if abs(ret_value - number) > abs(in_list[index] - number):
#     #         ret_value = in_list[index]
#     # return in_list.index(ret_value)
#
#
# print(index_of_nearest([], 17))
# print(index_of_nearest([7, 13, 3, 5, 18], 0))  # 2
# print(index_of_nearest([9, 5, 3, 2, 11], 4))  # 1
# print(index_of_nearest([7, 5, 4, 4, 3], 4))  # 2

# На вход программе подается строка текста, содержащая числа. Из данной строки формируется список чисел.
# Напишите программу, которая выводит те числа, которые повторяются в списке более одного раза.
# 4 8 0 3 4 2 0 3
# 0 3 4
in_list = [int(value) for value in input().split()]
print(*set([value for value in  in_list if in_list.count(value) > 1]))


