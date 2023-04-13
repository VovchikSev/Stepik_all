# образец из теории.
# def func_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("-- до выполнения функции")
#         res = func(*args, **kwargs)
#         print("-- после выполнения функции")
#         return res

#     return wrapper

# def some_func(title, tag):
#     print(f"title = {title}")
#     return f"<{tag}>{title}</{tag}>"

# some_func = func_decorator(some_func)
# some_func("some text")

# gпример с медленным алгоритмом евклида

# import time


# def test_time(func):  # декоратор проверки времени работы функции
#     def wrapper(*args, **kwargs):
#         st = time.time()
#         res = func(*args, **kwargs)
#         et = time.time()
#         print(f"время работы {et - st} сек.")
#         return res

#     return wrapper


# @test_time
# def get_nod(a, b):
#     while a != b:
#         if a > b:
#             a -= b
#         else:
#             b -= a
#     return a


# @test_time
# def get_fast_nod(a, b):
#     if a < b:
#         a, b = b, a
#     while b:
#         a, b = b, a % b
#     return a


# # get_nod = test_time(get_nod)
# # get_fast_nod = test_time(get_fast_nod)

# res = get_nod(2, 1000000)
# res2 = get_fast_nod(2, 1000000)

# print(res, res2)


# Подвиг 1. Объявите функцию с именем get_sq, которая вычисляет площадь прямоугольника по двум параметрам:
# width и height - ширина и высота прямоугольника. И возвращает результат (сама ничего на экран не выводит).
# То есть, функция имеет сигнатуру: def get_sq(width, height): ...
# Определите декоратор func_show для этой функции, который отображает результат на экране в виде строки (без кавычек):
# "Площадь прямоугольника: <значение>"

# def func_show (func):
#     def wrapper(*args, **kwargs):
#         print(f"Площадь прямоугольника: {func(*args, **kwargs)}")

#     return wrapper


# @func_show
# def get_sq(width, height):
#     return width * height

# res = get_sq(8, 11)


# Подвиг 2. На вход программы поступает строка с названиями пунктов меню, записанные в одну строчку через пробел.
# Необходимо задать функцию с именем get_menu, которая преобразует эту строку в список
# из слов и возвращает этот список. Сигнатура функции, следующая: def get_menu(s): ...
# Определите декоратор для этой функции с именем show_menu, который отображает список на экран в формате:
# 1. Пункт_1
# 2. Пункт_ ...


# def show_menu(func):
#     def wrapper(*args, **kwargs):
#         r_list = func(*args, **kwargs)
#         for index in range( len(r_list)):
#             print(f"{index + 1}. {r_list[index]}")
#     return wrapper

# @show_menu
# def get_menu(s):
#     return s.split()


# ret = get_menu(input())


# Подвиг 3. На вход программы поступает строка из целых чисел, записанных через пробел. Напишите функцию get_list, которая преобразовывает
# эту строку в список из целых чисел и возвращает его. Определите декоратор для этой функции, который сортирует список чисел по возрастанию.
# Результат сортировки должен возвращаться при вызове декоратора.
# Вызовите декорированную функцию get_list и отобразите полученный отсортированный список lst командой: print(*lst)
# 8 11 -5 4 3 10 -> -5 3 4 8 10 11


# def sort_list(func):
#     def wrapper(*args, **kwargs):
#         return sorted(func(*args, **kwargs))
#     return wrapper


# @sort_list
# def get_list(s: str):
#     return [int(value) for value in s.split()]


# ret = get_list
# print(*ret(input()))


# Подвиг 4. Вводятся две строки из слов (слова записаны через пробел). Объявите функцию, которая преобразовывает эти две строки в два списка слов
# и возвращает эти списки. Определите декоратор для этой функции, который из двух списков формирует словарь, в котором ключами являются слова из
# первого списка, а значениями - соответствующие элементы из второго списка. Полученный словарь должен возвращаться при вызове декоратора.
# Примените декоратор к первой функции и вызовите ее для введенных строк. Результат (словарь d) отобразите на экране командой:print(*sorted(d.items()))
# Sample Input: -- zip нам в помощь
# house river tree car
# дом река дерево машина

# def union_list(func):
#     def wrapper(*args, **kwargs):
#         l_en, l_ru = func(*args, **kwargs)
#         return dict(zip(l_en, l_ru))
#     return wrapper

# @union_list
# def fun_conv(EN, RU):
#     EN = EN.split()
#     RU = RU.split()
#     return EN, RU


# EN = input()
# RU = input()

# # d = fun_conv(EN, RU)
# # print(*sorted(d.items()))
# print(*sorted(fun_conv(EN, RU).items()))


# Подвиг 5. Объявите функцию, которая принимает строку на кириллице и преобразовывает ее в латиницу,
# используя следующий словарь для замены русских букв на соответствующее латинское написание:
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
# Функция должна возвращать преобразованную строку. Замены делать без учета регистра
# (исходную строку перевести в нижний регистр - малые буквы).
# Все небуквенные символы ": ;.,_" превращать в символ '-' (дефиса).
# Определите декоратор для этой функции, который несколько подряд идущих дефисов, превращает в один дефис.
# Полученная строка должна возвращаться при вызове декоратора. (Сам декоратор на экран ничего выводить не должен).
# Примените декоратор к первой функции и вызовите ее для введенной строки s на кириллице: s = input()


def decorator(function):
    def wrapper(text):
        message = function(text)
        while '--' in message:
            message = message.replace('--', '-')
        return message

    return wrapper


@decorator
def converter(text):
    result = []
    for char in text:
        if char in t:
            result.append(t[char])
        elif char in ": ;.,_":
            result.append("-")
        else:
            result.append(char)

    return ''.join(result)


s = input().lower()
print(converter(s))
