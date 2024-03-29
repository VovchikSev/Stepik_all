
# Подвиг 2. Объявите функцию с именем get_rect_value, которая принимает два аргумента (два числа) и еще один
# формальный параметр type с начальным значением 0. Если параметр type равен нулю, то функция должна возвращать
# периметр прямоугольника, а иначе - его площадь.

# def get_rect(len, height, type=0):
#     if type == 0:
#         return (len + height) * 2
#     else:
#         return len * height

# Подвиг 3. Объявите функцию с именем check_password, которая принимает аргумент - строку (пароль) и имеет
# один формальный параметр chars с начальным значением в виде строки "$%!?@#". Функция должна проверять:
# есть ли в пароле хотя бы один символ из chars и что длина пароля не менее 8 символов.
# Если проверка проходит, то функция возвращает True, иначе - False.
# 12345678! is-true
# def check_password (in_str:str, chars:str="$%!?@#")->bool:
#     if len(in_str) < 8:
#         return False
#     else:
#         return len(set(in_str) & set(chars)) > 0

# print(check_password("12345678!"))

# Подвиг 4. Объявите функцию, которая принимает строку на кириллице и преобразовывает ее в латиницу,
# используя следующий словарь для замены русских букв на соответствующее латинское написание:
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
# Функция должна возвращать преобразованную строку. Замены делать без учета регистра
# (исходную строку перевести в нижний регистр - малые буквы).
# У функции также определить формальный параметр sep с начальным значением в виде строки "-".
# Он будет определять символ для замены пробелов в строке.
# После объявления функции прочитайте (с помощью функции input) строку и дважды вызовите функцию
# (с выводом результата ее работы на экран):
# - первый раз только со строкой
# - второй раз со строкой и именованным аргументом sep со значением '+'.


# def replace_char(in_str: str, sep="-") -> str:
#     t[" "] = sep
#     result = ""
#     for value in in_str.lower():
#         if value in t.keys():
#             result += t[value]
#         else:
#             result += value
#     return result


# in_str = input()
# print(replace_char(in_str))
# print(replace_char(in_str, "+"))


# Подвиг 5. Объявите функцию, которая принимает строку и заключает ее в указанный тег. 
# Тег определяется формальным параметров tag с начальным значением в виде строки "h1". 
# Например, мы передаем строку "Hello Python" и заключаем в тег "h1". На выходе должны получить строку (без кавычек):
# "<h1>Hello Python</h1>"
# То есть, сначала открывается тег <h1>, а в конце строки - закрывается </h1>. И так для любых указанных тегов.
# После объявления функции прочитайте (с помощью функции input) строку и дважды вызовите функцию (с выводом результата 
# ее работы на экран):
# - первый раз только со строкой
# - второй раз со строкой и именованным аргументом tag со значением 'div'.

# def tag_creator(in_str:str, tag="h1"):
#     return f"<{tag}>{in_str}</{tag}>"

# in_str = input()
# print(tag_creator(in_str))
# print(tag_creator(in_str, "div"))


# Подвиг 6. Функции из предыдущего подвига 5 добавьте еще один формальный параметр up с начальным булевым значением True.
# Если параметр up равен True, то тег (указанный в формальном параметре tag) следует записывать заглавными буквами, 
# а иначе - малыми. После объявления функции прочитайте (с помощью функции input) строку и дважды вызовите функцию 
# (с выводом результата ее работы на экран): 
# - первый раз со строкой и именованным аргументом tag со значением 'div' 
# - второй раз со строкой, именованным аргументом tag со значением 'div' и именованным аргументом up со значением False.
def tag_creator(in_str:str, tag="div", up=True):
    if up:
        tag = tag.upper()
    return f"<{tag}>{in_str}</{tag}>"

in_str = input()
print(tag_creator(in_str))
print(tag_creator(in_str, up=False))