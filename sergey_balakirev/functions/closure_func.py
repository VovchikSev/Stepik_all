
# замыкания
# Подвиг 1. Используя замыкания функций, определите вложенную функцию, которая бы увеличивала значение
# переданного параметра на 5 и возвращала бы вычисленный результат. При этом внешняя функция должна иметь
# следующую сигнатуру: def counter_add(): ...


# def counter_add(in_param:int):
#     def inner_counter():
#         nonlocal in_param
#         in_param += 5
#         return in_param
#     return inner_counter

# k = int(input())
# cnt = counter_add(k)
# print(cnt())
# print(cnt())


# Подвиг 2. Используя замыкания функций, объявите внутреннюю функцию, которая увеличивает значение своего
# аргумента на некоторую величину n - параметр внешней функции с сигнатурой: def counter_add(n): ...
# Вызовите внешнюю функцию counter_add со значением аргумента 2 и результат присвойте переменной cnt.
# Вызовите внутреннюю функцию через переменную cnt со значением k, введенным с клавиатуры:


# def counter_add(in_param: int):
#     def inner_counter(in_adder: int) -> int:
#         nonlocal in_param
#         in_param += in_adder
#         return in_param
#     return inner_counter


# n = int(input())
# cnt = counter_add(2)
# print(cnt(n))


# Подвиг 3. Используя замыкания функций, объявите внутреннюю функцию,
# которая заключает в тег h1 строку s (s - строка, параметр внутренней функции).
# Далее, на вход программы поступает строка и ее нужно поместить в тег h1 с помощью реализованного замыкания.
# Результат выведите на экран.
# P. S. Пример добавления тега h1 к строке "Python": <h1>Python</h1>

# def outer_func(tag: str = "h1"):

#     def inner_func(in_str: str):
#         return f"<{tag}>{in_str}</{tag}>"
#         #  start + in_str + finish
#     return inner_func


# rec = outer_func(input())
# print(rec(input()))


# Подвиг 5. Используя замыкания функций, объявите внутреннюю функцию, которая преобразует строку из списка целых чисел, 
# записанных через пробел, либо в список, либо в кортеж. Тип коллекции определяется параметром tp внешней функции. 
# Если tp = 'list', то используется список, иначе (при другом значении) - кортеж.
# Далее, на вход программы поступают две строки: первая - это значение для параметра tp; вторая - список целых чисел, 
# записанных через пробел. С помощью реализованного замыкания преобразовать эти данные в соответствующую коллекцию. 
# Результат вывести на экран командой (lst - ссылка на коллекцию): print(lst)
# list
# -5 6 8 11 0 111 -456 3

