# 6  Множества, словари и кортежи
# 6.1 Словари Python. Операции и методы словаря
# 1
# in_value = int(input())
# my_dict = {}
# for value in range(1, in_value + 1):
#     my_dict[str(value)] = value ** 2
# print(my_dict)
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
# finded_key = ""
# for key, value in countries.items():
#     if city in value:
#         finded_key = key
#         break
#
# if len(finded_key) > 0:
#     print(f"INFO: {city} is a city in {finded_key}")
# else:
#     print(f"ERROR: Country for {city} not found")
