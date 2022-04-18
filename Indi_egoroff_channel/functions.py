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

def info_kwargs(**kwargs):
    [print(f'{k} = {v}') for k, v in sorted(kwargs.items())]


info_kwargs(first_name="John", last_name="Doe", age=33)
""" данный вызов печатает следующие строки
age = 33
first_name = John
last_name = Doe
"""