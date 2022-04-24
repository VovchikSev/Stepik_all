# 7 Функции
#
# 7.1 Определение и вызов функции. Инструкция def

# def summa_n(n: int):
#     # return sum([value for value in range(1, n + 1)])
#     print(f"Я знаю, что сумма чисел от 1 до {n} равна {sum([value for value in range(1, n + 1)])}")
#
# summa_n(int(input()))
#  3
# def check_password(password: str):
#     count_upper = 0
#     count_digit = 0
#     count_spec = 0
#
#     for ch in password:
#         if ch.isdigit():
#             count_digit += 1
#         if ch.isupper():
#             count_upper += 1
#         if ch in "!@#$%*":
#             count_spec += 1
#     flag = len(password) > 9 and count_digit > 2 and count_upper > 0 and count_spec > 0
#     print("Perfect password" if flag else "Easy peasy")


# def count_letters(in_str: str):
#
#     count_upper = 0
#     count_lower = 0
#     for ch in in_str:
#         if str.isalpha(ch):
#             print(f"IsAlpha({ch})")
#             if str.islower(ch):
#                 print(f"islower({ch})")
#                 count_lower += 1
#             if str.isupper(ch):
#                 print(f"isupper({ch})")
#                 count_upper += 1
#
#     print(f"Количество заглавных символов: {count_upper}")
#     print(f"Количество строчных символов: {count_lower}")
#
#
# count_letters("Привет, Старина")
# count_letters("QWERTY")

# 7.2 Зачем нужны функции в программировании

# 7.3 Возвращаемое значение функции. Оператор return

# def factorial(value: int) -> int:
#     factorial = 1
#     while value > 1:
#         factorial *= value
#         value -= 1
#     return factorial

# 7.3 Возвращаемое значение функции.
# 3

# def first_unique_char(in_str:str):
#     out_index = -1
#     for char in in_str:
#         if in_str.count(char) == 1:
#             out_index = in_str.index(char)
#             break
#     return out_index

# 7.4 Docstring, строка документирования
# 7.6 Область видимости: локальная, глобальная и встроенная

# def print_list(in_list: list):
#     if len(in_list) > 0:
#         print(in_list.pop(), end=" ")
#         print_list(in_list)
#
#
# my_len = int(input())
# print_list([int(value) for value in input().split()])

# def formula_fibonachi(n):
#     root_5 = 5 ** 0.5
#     phi = ((1 + root_5) / 2)
#
#     a = ((phi ** n) - ((-phi) ** -n)) / root_5
#
#     return round(a)

# def fibonacci(n):
#     if n <= 0:
#         print("Incorrect input")
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# num = int(input()) + 1
# print(fibonacci(num))

# def list_sum_recursive(sum_list):
#     if len(sum_list) == 0:
#         return 0
#     return sum_list.pop() + list_sum_recursive(sum_list)
#
#
# in_list = list(map(int, input().split()))
# print(list_sum_recursive(in_list))

# def flatten(in_list):
#     result_list = []
#     for i in in_list:
#         if type(i) is int:
#             result_list.append(i)
#         else:
#             result_list += flatten(i)
#     return result_list
#
#
# print(flatten([1, [2, 3, [4]], 5]))  # вернет [1,2,3,4,5]
# print(flatten([1, [2,3], [[2], 5], 6]))  # вернет [1,2,3,2,5,6]
# print(flatten([[[[9]]], [1,2], [[8]]]))  # вернет [9,1,2,8]

# 7.10 Рекурсия в Python. Рекурсивная функция Часть 2

# сортировка слиянием
# # функция merge_two_list должна объединить два списка
# def merge_two_list(a, b):
#     result_list = []
#     a_index = b_index = 0
#     while a_index < len(a) and b_index < len(b):
#         if a[a_index] < b[b_index]:
#             result_list.append(a[a_index])
#             a_index += 1
#         else:
#             result_list.append(b[b_index])
#             b_index += 1
#
#     if a_index < len(a):
#         result_list += a[a_index:]
#     if b_index < len(b):
#         result_list += b[b_index:]
#
#     return result_list
#
# # функция merge_sort должна выполнить сортировку
# def merge_sort(s):
#     if len(s) == 1:
#         return s
#     middle = len(s) // 2
#     left_half = merge_sort(s[:middle])
#     right_half = merge_sort(s[middle:])
#     return merge_two_list(left_half, right_half)
#
#
# in_trash = [6, 2, 19, 5, 10, 7, 11]
# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# print(merge_sort(alist))
# print(alist)

# быстрая сортировка
# # функция quick_sort должна выполнить сортировку
# def quick_sort(s):
#     if len(s) <= 1:
#         return s
#     element = s[len(s) // 2]
#     left_list = list(filter(lambda value: value < element, s))
#     center_list = [value for value in s if value == element]  # list(filter(lambda value: value == element, s))
#     right_list = list(filter(lambda value: value > element, s))
#
#     return quick_sort(left_list) + center_list + quick_sort(right_list)
#
#
# in_trash = [6, 2, 19, 5, 10, 7, 11]
# print(quick_sort(in_trash))


def multiply(value):
    def inner(multiplicator):
        return value * multiplicator

    return inner

f_2 = multiply(2)
print("Умножение 2 на 5 =", f_2(5))  #10
print("Умножение 2 на 15 =", f_2(15))  #30
f_3 = multiply(3)
print("Умножение 3 на 5 =", f_3(5))  #15
print("Умножение 3 на 15 =", f_3(15))  #45
