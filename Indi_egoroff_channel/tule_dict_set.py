# 6  Множества, словари и кортежи
# 6.1 Словари Python. Операции и методы словаря
# 1
# in_value = int(input())
# my_dict = {}
# for value in range(1, in_value + 1):
#     my_dict[str(value)] = value ** 2
# print(my_dict)
# print({a: a ** 2 for a in range(1, int(input()) + 1)}) аналог вывода сгенерированного словаря
#
# 2
# index = 97
# alphabet = {}
# while chr(index) <= 'z':
#     alphabet[chr(index)] = index - 96
#     index += 1
# for key, value in alphabet.items():
#     print(key, value)
#
# 3
# d1 = {'a': 100, 'b': 200, 'c': 333}
# d2 = {'x': 300, 'y': 200, 'z': 777}
# rez = d1.copy()
# rez.update(d2)
# print(rez)
#
# 4
# logins = {}
# for _ in range(int(input())):
#     login = input()
#     if login in logins:
#         print(f"{login}{logins[login]}")
#         logins[login] += 1
#     else:
#         print("OK")
#         logins[login] = 1
#
# 5
# countries = {
#     "Sweden": ["Stockholm", "Göteborg", "Malmö"],
#     "Norway": ["Oslo", "Bergen", "Trondheim"],
#     "England": ["London", "Birmingham", "Manchester"],
#     "Germany": ["Berlin", "Hamburg", "Munich"],
#     "France": ["Paris", "Marseille", "Toulouse"]
# }
# city = input()
# find_key = ""
# for key, value in countries.items():
#     if city in value:
#         find_key = key
#         break
#
# if len(find_key) > 0:
#     print(f"INFO: {city} is a city in {find_key}")
# else:
#     print(f"ERROR: Country for {city} not found")
#
# 6.2 Ситуации, где полезно использовать словарь
# 2
# in_word = "ZZzzzZ34 WWw777"  # input()
# my_dict = {}
# for ch in in_word:
#     if ch.isalpha():
#         my_dict[ch.lower()] = my_dict.get(ch.lower(), 0) + 1
# print(my_dict)

# 3
#
# data = {'my_friends': {'count': 10, 'items':
#     [{'first_name': 'Kurt', 'id': 621547005, 'last_name': 'Cobain', 'bdate': '31.8.2005'},
#     {'first_name': 'Виолетта', 'id': 484200150, 'last_name': 'Кастилио'},
#     {'first_name': 'Иринка', 'id': 21886133, 'last_name': 'Бушуева', 'bdate': '28.8.1942'},
#     {'first_name': 'Данил', 'id': 282456573, 'last_name': 'Греков', 'bdate': '4.7.2002'},
#     {'first_name': 'Валентин', 'id': 184902932, 'last_name': 'Долматов', 'bdate': '25.5'},
#     {'first_name': 'Евгений', 'id': 620469646, 'last_name': 'Шапорин', 'bdate': '6.12.1982'},
#     {'first_name': 'Ангелина', 'id': 622328862, 'last_name': 'Краснова', 'bdate': '4.11.1995'},
#     {'first_name': 'Иван', 'id': 576015198, 'last_name': 'Вирин', 'bdate': '2.2.1915'},
#     {'first_name': 'Паша', 'id': 386922406, 'last_name': 'Воронов', 'bdate': '27.9'},
#     {'first_name': 'Ольга', 'id': 622170942, 'last_name': 'Савченкова', 'bdate': '20.12'}]}}
# out_list = []
# for i in data['my_friends']['items']:
#     out_list.append(i['first_name'])
# print(*sorted(out_list), sep='\n')

# 4

# def get_dict(a_str: str) -> dict:
#     result = {}
#     for ch in a_str:
#         result[ch.lower()] = result.get(ch.lower(), 0) + 1
#     return result
#
#
# print("YES" if get_dict(input()) == get_dict(input()) else "NO")
#
# 5

# morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
#          'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
#          'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
#          'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
#          'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
#          'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
#          'y': '—•——', 'z': '——••'}
# in_str = "Houston we have a problem".lower() # input().lower()
# # out_list = []
# for word in in_str.split():
#     # print(word)
#     # out_list.append(" ".join([morze[val] for val in word]))
#     print(" ".join([morze[val] for val in word]))
# # print(*out_list, sep="\n")

# 6.4 кортежи
my_tuple = (-214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781, 759, -593, 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791, 631, -493, -218, -829, -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933, -254, 307, -493, -419, -109, -543, 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278, 867, 321, -20, -415, -357, 735, -906, -14, -370, 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472, -986, -964, -73, 29)
# 3
# print(min(my_tuple), max(my_tuple))
# 4
# my_sum = [val for val in my_tuple if bool(val % 2)]
# print(sum(my_sum) / len(my_sum))
# 4
# print(tuple([i for i in range(int(input()), int(input())+1)]))
# 5
in_value = int(input())
print(tuple([i for i in range(in_value, (in_value ** 2) + 1)]))
