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

import json

max_sale = 0
max_name = ''
max_last_name = ''
with open("f:/manager_sales.json", "r", encoding='utf-8') as file:
    js_data = json.load(file)
    for element in js_data:

        name = element["manager"]["first_name"]
        last_name = element["manager"]["last_name"]
        total = 0
        for car in element["cars"]:
            total += car["price"]


        if total > max_sale:
            max_sale = total
            max_name = name
            max_last_name = last_name

    print(max_name, max_last_name, max_sale)