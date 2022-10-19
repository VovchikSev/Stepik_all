# пример из теории
# from math import sin, pi
#
#
# def df_decorator(dx=0.01):
#     def func_decorator(func):
#         def wrapper(x, *args, **kwargs):
#             res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
#             return res
#
#         return wraper
#
#     return func_decorator
#
#
# @df_decorator(dx=0.00000001)
# def sin_dx(x):
#     return sin(x)
#
#
# df = sin_dx(pi / 3)
# print(df)

# Подвиг 1. Вводится строка целых чисел через пробел. Напишите функцию, которая преобразовывает эту строку в
# список чисел и возвращает их сумму. Определите декоратор для этой функции, который имеет один параметр start -
# начальное значение суммы.
# Примените декоратор со значением start=5 к функции и вызовите декорированную функцию
# для введенной строки s: s = input()
# Результат отобразите на экране.

# def pre_decorator(start):
#     def decorator(function):
#         def wrapper(message):
#             return function(message) + start
#         return wrapper
#     return decorator
#
#
# @pre_decorator(start=5)
# def modificate(text):
#     text = [int(i) for i in text.split()]
#     return sum(text)
#
#
# s = input()
# result = modificate(s)
# print(result)

"""
Подвиг 2. Объявите функцию, которая возвращает переданную ей строку в нижнем регистре (с малыми буквами).
Определите декоратор для этой функции, который имеет один параметр tag, определяющий строку с названием тега и начальным
значением "h1". Этот декоратор должен заключать возвращенную функцией строку в теге tag и возвращать результат.
Пример заключения строки "python" в тег h1: <h1>python</h1>
Примените декоратор со значением tag="div" к функции и вызовите декорированную функцию для введенной строки s:
s = input()
Результат отобразите на экране.
Sample Input: Декораторы - это классно! -> <div>декораторы - это классно!</div>
"""

# def pre_decorator(tag: str = "h1"):
#     def in_decorator(func):
#         def wrapper(message: str) -> str:
#             return f"<{tag}>{func(message)}</{tag}>"
#         return wrapper
#
#     return in_decorator
#
#
# @pre_decorator(tag="div")
# def prepare_str(s: str) -> str:
#     return s.lower()
#
# print(prepare_str(input()))


"""
Подвиг 3. Объявите функцию, которая принимает строку на кириллице и преобразовывает ее в латиницу, используя следующий 
словарь для замены русских букв на соответствующее латинское написание:
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
Функция должна возвращать преобразованную строку. Замены делать без учета регистра (исходную строку перевести в нижний 
регистр - малые буквы).
Определите декоратор с параметром chars и начальным значением " !?", который данные символы преобразует в символ "-" и, 
кроме того, все подряд идущие дефисы (например, "--" или "---") приводит к одному дефису. Полученный результат должен 
возвращаться в виде строки.
Примените декоратор с аргументом chars="?!:;,. " к функции и вызовите декорированную функцию для введенной строки s:
s = input()
Результат отобразите на экране.
Sample Input: Декораторы - это круто!  Sample Output: dekoratory-eto-kruto-
"""

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def pre_decorator(chars=" !?"):
    def decorator(function):
        def wrapper(message):
            result = ""
            in_str = function(message)

            for char in in_str:
                if char in chars:
                    result += '-'
                else:
                    result += char

            while "--" in result:
                result = result.replace("--", "-")

            return result

        return wrapper

    return decorator


@pre_decorator(chars="?!:;,. ")
def converter(text):
    text = text.lower()
    result = ""
    for char in text:
        if char in t:
            result += t[char]
        else:
            result += char
    return result


print(converter(input()))
