# # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# # [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # numbers2 = list(map(lambda val:val*val, numbers))
# print(list(map(lambda val:val*val, numbers)))
# print(list(map(lambda val:val**3, numbers)))

# def file_read(file_name):
#     with open(file_name, 'r', encoding='utf-8') as file:
#         print(file.read())


# def longest_word_in_file(file_name):
#     def remove_punctuation(word_: str):
#         from string import punctuation
#         for punc in punctuation:
#             if punc in word_:
#                 word_ = word_.replace(punc, '')
#         return word_
#
#     result = ""
#     with open(file_name, 'r', encoding='utf-8') as file:
#         for line in file:
#             words = line.split()
#             # print(words, len(words))
#             for word in words:
#                 word = remove_punctuation(word)
#                 if len(word) >= len(result):
#                     result = word
#     return result
#
#
# print(longest_word_in_file("f:/text.txt"))
# tree_ = []
# two_ = []
# with open("f:/numbers.txt", 'r', encoding='utf-8') as file:
#     for txt_num in file:
#         txt_num = txt_num.strip()
#         if len(txt_num) == 2:
#             print(txt_num)
#             two_.append(int(txt_num))
#         elif len(txt_num) == 3:
#             print(txt_num)
#             tree_.append(int(txt_num))
# print(len(tree_), sum(two_))

# import json
# max_sale = 0
# max_name = ''
# max_last_name = ''
# with open("f:/manager_sales.json", "r", encoding='utf-8') as file:
#     js_data = json.load(file)
#     for element in js_data:
#
#         name = element["manager"]["first_name"]
#         last_name = element["manager"]["last_name"]
#         total = 0
#         for car in element["cars"]:
#             total += car["price"]
#         if total > max_sale:
#             max_sale = total
#             max_name = name
#             max_last_name = last_name
#     print(max_name, max_last_name, max_sale)

# import json
# group_id = 0
# womans = 0
#
# with open("f:/group_people.json", "r", encoding='utf-8') as file:
#     js_data = json.load(file)
#     for element in js_data:
#         # print(element)
#         tmp_id = element['id_group']
#         woman_in_group = 0
#         for person in element['people']:
#             print(person)
#             if person['gender'] == 'Female' and person['year'] > 1977:
#                 woman_in_group += 1
#         if woman_in_group > womans:
#             womans = woman_in_group
#             group_id = tmp_id
# print(group_id, womans) # ответ 9 10

# import json
# js_data = {}
# lines = []

# with open("f:/Alphabet.json", "r", encoding='utf-8') as file:
#     js_data = json.load(file)
#
# with open("f:/Abracadabra.txt", "r", encoding='utf-8') as file:
#     for ch in file.read():
#         if ch in js_data.keys():
#             ch = js_data.get(ch)
#         print(ch, end="")

# https://stepik.org/lesson/372111/step/2?unit=359665
# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93),('History', 82)]
# # print(sorted(subject_marks, key=lambda x: x[1]), sep="\n")
# [print(*value) for value in sorted(subject_marks, key=lambda x: x[1])]

# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97),
#                  ('Physics', 93), ('History', 82), ('French', 78),
#                  ('Art', 58), ('Chemistry', 76), ('Programming', 91)]
# [print(*value) for value in sorted(subject_marks, key=lambda x: x[1], reverse=True)]

# subject_marks = [('English', 88), ('Science', 90), ('Maths', 88),
#                  ('Physics', 93), ('History', 78), ('French', 78),
#                  ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
# new_list = sorted(subject_marks, key=lambda x: x[0].lower(),)
# [print(*value) for value in sorted(new_list, key=lambda x:x[1], reverse=True)]

# не сдано----------------------------------------------------
# models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
#           {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
#           {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
#           {'make': 'Apple', 'model': 10, 'color': 'Silver'},
#           {'make': 'Oppo', 'model': 9, 'color': 'Red'},
#           {'make': 'Huawei', 'model': 4, 'color': 'Grey'},
#           {'make': 'Honor', 'model': 3, 'color': 'Black'}]
#
# for device in sorted(models, key=lambda val: val['color']):
#     print(f"Производитель: {device['make']}, модель: {device['model']}, цвет: {device['color']}")

# in_dict = {}
# while True:
#     in_str = input()
#     if in_str == "конец":
#         break
#     name, cost = in_str.split(": ")
#     in_dict[name] = int(cost)
#
# for name, cost in sorted(in_dict.items(), key=lambda val: val[1], reverse=True):
#     print(name, cost)

my_dict = {}
for _ in range(int(input())):
    in_value = input()
    my_dict[in_value] = my_dict.get(in_value, 0) + 1

max_awards = sorted(my_dict.items(), key=lambda val: val[1], reverse=True)[0]
min_awards = sorted(my_dict.items(), key=lambda val: val[1])[0]

print(*max_awards, sep=", ")
print(*min_awards, sep=", ")

# my_dict = {}
# for _ in range(int(input())):
#     number, name = input().split()
#     my_dict.setdefault(name, [])
#     my_dict[name].append(number)
#
# for _ in range(int(input())):
#     name = input()
#     if name in my_dict.keys():
#         print(*my_dict[name])
#     else:
#         print("Неизвестный номер")

# my_dict = {}
# for _ in range(int(input())):
#     name, day, month = input().split()
#     my_dict[month] = my_dict.get(month, []) + [name]
#
# for _ in range(int(input())):
#     month = input()
#     if month in my_dict.keys():
#         print(*sorted(my_dict[month]))
#     else:
#         print("Нет данных")

# my_dict = {}
# while True:
#     in_value = input()
#     if in_value == "конец":
#         break
#     name, rank = in_value.split(", ")
#     my_dict[name] = my_dict.get(name, []) + [int(rank)]
#
# res_dict = {}
# for key, value in sorted(my_dict.items()):
#     res_dict[key] = sum(value) / len(value)
#
# # for value in sorted(my_dict.items(), key=lambda val: (val[1], val[0])):
# for value in sorted(res_dict.items(), key=lambda p: p[1], reverse=True):
#     print(*value)

