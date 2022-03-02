# итоговая работа про словари
# my_dict = {}
# in_list = []
# for _ in range(int(input())):
#     in_list.append(input().split())
#
#
# for val_list in in_list:
#     if my_dict.get(val_list[0]):
#         pass
#     else:
#         my_dict.setdefault(val_list[0], dict())
#
#     new_dict = my_dict.get(val_list[0])
#     amount = int(val_list[2])
#     new_dict.setdefault(val_list[1], 0)
#     new_dict[val_list[1]] += amount
#     my_dict[val_list[0]] = new_dict
#
# list_buyer = sorted(my_dict.keys())
# # print(* list_buyer)
# for buyer in list_buyer:
#    list_key = sorted(my_dict[buyer].keys())
#    print(buyer, ":", sep="")
#    for k in list_key:
#        print(k, my_dict[buyer].get(k))
# краткое красивое решение
# data = {}
# for _ in range(int(input())):
#     name, product, count = input().split()
#     data.setdefault(name, {})
#     data[name][product] = data[name].get(product, 0) + int(count)
#
# for person, products in sorted(data.items()):
#     print(f'{person}:')
#     for product, count in sorted(products.items()):
#         print(product, count)



# У нас еще не было данного покупателя: нужно добавить покупателя и первую покупку (подсловарь)
# У нас был уже покупатель, но не было данного товара: расширить подсловарь
# У нас уже этот покупатель покупал данный товар: изменить значение в подсловаре по наименованию товара
# (увеличить число купленных товаров)
# Вывод данных
# Формируем отсортированный список покупателей и перебиваем его
# Выводим имя покупателя
# Формируем отсортированный список купленных им товаров и перебираем его
# Выводим наименование товара и его количество



# my_dict = {'write': 'W', 'read': 'R', 'execute': 'X'}
# files_dict = {}
#
# for _ in range(int(input())):
#     in_str = input().split()
#     files_dict[in_str[0]] = in_str[1:]
# for _ in range(int(input())):
#     in_str = input().split()
#     if my_dict.get(in_str[0]) in files_dict[in_str[1]]:
#         print("OK")
#     else:
#         print("Access denied")


# def merge(values):      # values - это список словарей
#     res_dict = {}
#     for cur_dict in values:
#         for key, value in cur_dict.items():
#             res_dict.setdefault(key, set()).add(cur_dict[key])
#     return res_dict
#
# result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
# print(merge({}))


# def build_query_string(params):
#     lis_r = []
#     for key in sorted(params.keys()):
#         lis_r.append(key + "=" + str(params.get(key)))
#     return "&".join(lis_r)
#     #  красиво
#     # res = [f'{k}={v}' for k, v in params.items()]
#     # return '&'.join(sorted(res))
#
# print(build_query_string({'name': 'timur', 'age': 28}))
# print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))

# аналог с коротким словарем на два цикла
# d = {
#     1: "AEILNORSTU",
#     2: "DG",
#     3: "BCMP",
#     4: "FHVWY",
#     5: "K",
#     8: "JX",
#     10: "QZ"
# }
#
# print(sum([k for i in input() for k, v in d.items() if i in v]))


# count_dic ={}
# for word in input().split():
#     count_dic[word] = count_dic.get(word, 0) + 1
#     print(count_dic.get(word), end=" ")


# dnk_rnk ={"G": "C",
#           "C": "G",
#           "T": "A",
#           "A": "U"}
#
# print(*[dnk_rnk.get(ch) for ch in input()], sep="")
# # это тоже работает, с троку красивее
# # out_str = ""
# # for ch in input():
# #     out_str += dnk_rnk.get(ch)
# # print(out_str)


# # Дополните приведенный код, чтобы он вывел все электронные адреса в алфавитном порядке, каждый на отдельной строке,
# # в формате username@domain.
# emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
#           'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
#           'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
#           'yandex.ru': ['surface', 'google'],
#           'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
#           'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
# result = []
# for key, value in emails.items():
#     for mail in value:
#         result.append(mail + "@" + key)
#
# print(*sorted(result), sep="\n")
# # однострочник
# # print(*sorted([i+'@'+k for k, v in emails.items() for i in v]), sep = '\n')


# Дополните приведенный код, чтобы в списках значений элементов словаря my_dict  не было чисел, больших 20.
# При этом порядок оставшихся элементов меняться не должен.
# my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21],
#            'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42],
#            'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}
# print(my_dict.items())
# for key, edit_list in my_dict.items():
#     my_dict[key] = [value for value in edit_list if value < 20]
# # однострочник
# # my_dict = {k: [i for i in v if i <= 20] for k, v in my_dict.items()}
#
# print(my_dict.items())


# итоговая работа про словари

# student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
# student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
# student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]
#
# result = []
# # интересно
# # result = [{key: {key_2: value}} for key, key_2, value in zip(student_ids, student_names, student_grades)]
# # однострочник примерно аналогичный
# # result = [{student_ids[i]: {student_names[i]: student_grades[i]}} for i in range(len(student_grades))]
# for index in range(len(student_ids)):
#     print(student_ids[index], student_names[index], student_grades[index])
#     result.append({student_ids[index]: {student_names[index]: student_grades[index]}})
# print(result)


# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
#
# result = {value[0]: value[1:] for value in tuples}
# print(tuples)
# print(result)


# students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50), 'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80), 'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}
# result = {key: value for key, value in students.items() if value[0]  > 167 and value[1] < 75}
# print(result)


# letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}
# remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
# # result = {}
# result = {key: value for key, value in letters.items() if key not  in remove_keys}
# # красота
# # result = {k: letters[k] for k in set(letters) - set(remove_keys)}
# print(result)

# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
#
# result = {}
# for key in words:
#     result[key] = [ord(char) for char in key]
# # в одну строку
# # result = {word: [ord(letter) for letter in word] for word in words}
# print(result)


# # numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
# numbers = [1, 6, 18]
# result = {}
# for value in numbers:
#     val_list = [1]
#     if value > 2:
#         val_list.append(value)
#     for delimiter in range(2, (value // 2) + 1):
#         if value % delimiter == 0:
#             val_list.append(delimiter)
#     result[value] = sorted(val_list)
# # аналог в одну строку
# # result = {i: [j for j in range(1, i + 1) if i % j == 0] for i in numbers}

# print(result)
# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
# result = {}
# for word in s.split():
#     key, value = word.split(":")
#     result[int(key)] = value
# # цикл в одну строку
# # result = {int(k):v for k, v in [l.split(':') for l in s.split()]}
# # result = {int(i.split(':')[0]) : i.split(':')[1] for i in s.split(' ')}
# print(result)


# months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
#
# result = {value: key for key, value in months.items()}
# print(result)


# favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62, 'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654, 'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271, 'anna': 55, 'madlen': 876}
# result = {k: favorite_numbers[k] for k in favorite_numbers if 100 > favorite_numbers[k] > 9}
# # немного другой вариант разбора
# # result = {a: b for a, b in favorite_numbers.items() if 9 < b < 100}
# print(*result.items(), sep="\n")


# colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange', 'c8': None, 'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl', 'c21': None, 'c22': 'Sand', 'c23': None}
# result = {}
# # в одну строку для примера сохраню
# # result = {k: colors[k] for k in colors if colors[k]}
# for i in colors:
#     if colors[i]:
#         result[i] = colors[i]
# print(result)


# my_key = input()
# my_dic = {}
# for _ in range(int(input())):
#     value, key = input().split(": ")
#     my_dic[int(key)] = value
# my_set = set(my_key)
# print(my_dic)
# new_str = ""
# for ch in my_key:
#     new_str += my_dic.get(my_key.count(ch))
#
# print(new_str)


# my_dict = {}
# for _ in range(int(input())):
#     num, name = input().lower().split()
#     my_dict.setdefault(name, []).append(num)
#
# for _ in range(int(input())): # условно работающий метод, тредует доп ввода в среде, но проходит проверку.
#     print(*my_dict.get(input().lower(), ['абонент не найден']))
# # result = []
# # for _ in range(int(input())):
# #     result.append(my_dict.get(input().lower(), ""))
# # for out in result:
# #     if out == "":
# #         print("абонент не найден")
# #     else:
# #         print(*out)
# #     # print( (*out) if out != "" else "абонент не найден")
# # print(result)


# my_dict = {}
# for _ in range(int(input())):
#     land = input().split()
#     my_dict[land[0]] = land[1:]
# result = []
# for _ in range(int(input())):
#     in_city = input()
#     for key, values in my_dict.items():
#         if in_city in values:
#             result.append(key)
#             break
# print(*result, sep="\n")

# более симпатичное решение
# d = {}
# for _ in range(int(input())):
#     country, *cities = input().split()
#     d.update(dict.fromkeys(cities, country))
# for _ in range(int(input())):
#     print(d[input()])



# my_dict1 = {}
# for _ in range(int(input())):
#     in_val = input().split()
#     my_dict1[in_val[1]] = in_val[0]
#     my_dict1[in_val[0]] = in_val[1]
#
# print(my_dict1.get(input()))

# str1 = input().lower()
# str2 = input().lower()
# my_dict = {}
# # print(str1)
# # print(str2)
# for char in str1:
#     if char not in " .,!?:;-":
#         my_dict[char] = my_dict.get(char, 0) + 1
# for char in str2.strip(" .,!?:;-"):
#     if char not in " .,!?:;-":
#         my_dict[char] = my_dict.get(char, 0) - 1
# print(('NO', 'YES')[set(my_dict.values()) == {0}])
# print("YES" if sorted(str1) == sorted(str2) else 'NO')

# print("YES" if sorted(input()) == sorted(input()) else 'NO')
#  хоть и не такое короткое решение, но про словари и красивое
# d = {}
# for c in input().lower():
#     d[c] = d.get(c, 0) + 1
# for c in input().lower():
#     d[c] = d.get(c, 0) - 1
#
# print(('NO', 'YES')[set(d.values()) == {0}])

# my_dict = {}
# for _ in range(int(input())):
#     in_str = input().split(": ")
#     my_dict[in_str[0].lower()] = in_str[1]
# # print(my_dict)
# list_ask = [input() for _ in range(int(input()))]
# for ask in list_ask:
#     print(my_dict.get(ask.lower(), "Не найдено"))


# chars = [char for char in input().split()]
# res_chars = []
# for ch in chars:
#     if ch in res_chars:
#         print(f"{ch}_{res_chars.count(ch)}", end=" ")
#     else:
#         print(ch, end=" ")
#     res_chars.append(ch)


# words = [word.strip(".,!?:;-") for word in input().lower().split()]
# result = {}
# for word in words:
#     result[word] = words.count(word)
# print(min([key for key, value in result.items() if value == min(result.values())]))
# # более правильное решение для словарей.
# d = {}
# for w in input().split():
#     w = w.strip('.,!?:;-').lower()
#     d[w] = d.get(w, 0) + 1  # добавить по ключу со значением по умолчанию (когда нет  значения) = 0 и прибавить к значению словаря 1 по ключу.
# print(min(d.items(), key=lambda x: (x[1], x[0]))[0]) # это менее понятно, но и тут разобраться можно или оставить мое решение на вывод


# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
# # кличка собаки, имя владельца, фамилия владельца, возраст владельца
# result = {}
# for item in pets:
#     result.setdefault(item[1:], []).append(item[0])
# print(result)



# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
# result = {key: s.split().count(key) for key in set(s.split())}
# my_list = []
# for my_key, value in result.items():
#     if value == max(result.values()):
#         my_list.append(my_key)
# print(min(my_list))
# #  немного иначе и интересен цикл наполнения списка
# # max_value = max(result.values())
# # word = [key for key, value in result.items() if value == max_value]
# # print(min(word))
# # аналог в одну строку
# # print(min([key for key, val in dict_s.items() if val == max(dict_s.values())]))


# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
#
# result = {}
# for char in text:
#     if char not in result.keys():
#         result[char] = text.count(char)
# # в одну строку
# # result = {key: text.count(key) for key in set(text)}
# print(result)


# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
#
# # result = dict1.copy()
# # result.update(dict2)
# # for key in result.keys():
# #     if key in dict1.keys() and key in dict2:
# #         result[key] = dict1[key] + dict2[key]
# # более элегантное решение
# result = dict1.copy()
# for key, value in dict2.items():
#     result[key] = result.get(key, 0) + value
# print(result.items())


# result = {}
# result = dict ([(tuple([digit, digit*digit] )) for digit in [val for val in range(1, 16)]])
# # аналог но более красивый
# # result = {key: key ** 2 for key in range(1, 16)}
# print(result)



# info1 = {'name': 'Bob',
#         'age': 25,
#         'job': 'Dev'}
#
# info2 = {'age': 30,
#         'city': 'New York',
#         'email': 'bob@web.com'}
# print(info1)
# info1.update(info2)
# print(info1)
# print(info1.get('kki'))
# print(info1)

# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
#          '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---',
#          '...--', '....-', '.....', '-....', '--...', '---..', '----.']
# out_str = []
# for char in input().upper():
#     if char in letters:
#         out_str.append(morse[letters.index(char)])
#
# print(*out_str)
# то же в одну строку
# print(*[morse[letters.index(elem)] for elem in input().upper() if elem in letters])

# d2 = {".":'1', ",":'11', "?":'111', "!":'1111', ":":'11111',
#       "A":'2', "B":'22', "C":'222',
#       "D":'3', "E":'33', "F":'333',
#       "G":'4', "H":'44', "I":'444',
#       "J":'5', "K":'55', "L":'555',
#       "M":'6', "N":'66', "O":'666',
#       "P":'7', "Q":'77', "R":'777', "S": '7777',
#       "T":'8', "U":'88', "V":'888',
#       "W":'9', "X":'99', "Y":'999', "Z": '9999',
#       " ":'0'}
#
# .- --. . -. - ----- ----- --...
# .- --. . -. - ----- ----- --...
# in_str = input().upper()
# out_str = ""
# for char in in_str:
#     if char not in ['"', "'"]:
#         out_str += d2[char]
# print(out_str)
# более красивое решение.
# keyboard = {
#     "1": ".,?!:",
#     "2": "ABC",
#     "3": "DEF",
#     "4": "GHI",
#     "5": "JKL",
#     "6": "MNO",
#     "7": "PQRS",
#     "8": "TUV",
#     "9": "WXYZ",
#     "0": " "
# }
# for letter in input().upper():
#     for key, value in keyboard.items():
#         if letter in value:
#             print(key * (value.index(letter) + 1), end="")


# courses = {'CS101': [3004, 'Хайнс', '8:00'],
#            'CS102': [4501, 'Альварадо', '9:00'],
#            'CS103': [6755, 'Рич', '10:00'],
#            'NT110': [1244, 'Берк', '11:00'],
#            'CM241': [1411, 'Ли', '13:00']}
# in_value = input()
# print("{}: {}, {}, {}".format(in_value, *courses[in_value]))


# my_dict = {"0": "zero", "1": "one",  "2": "two", "3": "three", "4": "four", "5": "five",
#            "6": "six", "7": "seven", "8": "eight", "9": "nine"}
# my_list = []
# for leter in input():
#     my_list.append(my_dict.get(leter))

# print(*my_list)

# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
# # result = [user['name'] for user in users if len(user) == 2 or user['email'] == ""]
# print(*sorted([user['name'] for user in users if len(user) == 2 or user['email'] == ""]))
# # print(*sorted([value.get('name') for value in users if len(value) == 2 ])))
# # print([[value, len(value)] for value in users], sep='\n')