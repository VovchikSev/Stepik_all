


# import random
# with open('d:/output.txt', 'w') as file:
#     for _ in range(25):
#         print(random.randint(111, 778), file=file)
# аналог в одну строку
# from random import sample as r
# print(*r(range(111, 778), 25), file=open('random.txt', 'w'), sep='\n')


# with open('d:/output.txt', 'w') as file:
#     print(input(), file=file)

# def read_csv():
#     with open("d:/data.csv", 'rt', encoding='utf-8') as data_file:
#         names_list = data_file.readline().strip().split(",")   # list(map(str.strip, data_file.readline()))
#         data_list = list(map(str.strip, data_file.readlines()))
#         dict_list = []
#         for data_row in data_list:
#             dict_list.append(dict(zip(names_list, data_row.split(","))))
#         print(dict_list[9])
#         print(*names_list, sep="\n")
# read_csv()


# with open("d:/population.txt ", 'rt', encoding='utf-8') as names_file:
#     full_countries = list(map(str.strip, names_file.readlines()))
#     filtered_list = []
#     for value in full_countries:
#         name, population = value.split("\t")
#         if name.startswith("G") and int(population) > 500_000:
#             print(name)
#
# print(*full_countries, sep="\n")


# from random import choice
# with open("d:/file.txt ", 'rt', encoding='utf-8') as names_file:
#     with open("d:/file2.txt ", 'rt', encoding='utf-8') as last_names_file:
#         names_list = list(map(str.strip, names_file.readlines()))
#         last_names_list = list(map(str.strip, last_names_file.readlines()))
#         fill_lis = [print(f'{choice(names_list)} {choice(last_names_list)}') for _ in range(3)]
# print(names_list)
# print(last_names_list)


# import re
# with open("d:/file.txt ", 'rt', encoding='utf-8') as my_file:
#     my_list = list(map(str.strip, my_file.readlines()))
#     words = 0
#     letters = 0
#     for value in my_list:
#         words += len(value.split())
#         letters += len(re.sub("[^A-Za-z]", "", value))
#     print("Input file contains:")
#     print(f'{letters} letters')
#     print(f'{words} words ')
#     print(f'{len(my_list)} lines')


# import re
# with open("input.txt", 'rt', encoding='utf-8') as my_file:
#     my_list = list( map(lambda value: str.strip(value), my_file.readlines()))
#     sum_list = 0
#
#     for index in range(len(my_list)):
#         my_list[index] = re.sub("[^0-9]", " ", my_list[index]).split()
#         my_list[index] = list(map(int, my_list[index]))
#         print(my_list[index])
#         sum_list += sum(my_list[index])
#
#     print(sum_list)


# суммы чисел в строках
# with open("input.txt", 'rt', encoding='utf-8') as my_file:
#     my_list = list(map(lambda value: value.split(),my_file.readlines()))
#     for value in my_list:
#         print(sum(map(int, value)))
#     print(my_list)

# with open("input.txt", "rt", encoding='utf-8') as my_file:
#     list_lines = list( map(lambda value: str.strip(value), my_file.readlines()))
#     max_len = max(map(lambda value: len(value), list_lines))
#     print(*list(filter(lambda value: len(value) == max_len, list_lines)), sep='\n')




# with open("nums.txt", 'rt', encoding='utf-8') as my_file:
#     my_lines = list(map(lambda value: value.strip(), my_file.readlines()))
#     # new_list = map(lambda name, amount, cost: int(amount) * int(cost), my_lines)
#     my_sum = 0
#     for value in my_lines:
#         my_sum += int(value.split("\t")[1]) * int(value.split("\t")[2])
#     print(my_sum)


# with open("nums.txt", 'rt', encoding='utf-8') as my_file:
#     # my_list = list(map(int, filter(lambda x: x.strip(' ') != "\n", my_file.readlines())))
#     print(sum(map(int, filter(lambda x: x.strip(' ') != "\n", my_file.readlines()))))

# with open("nums.txt", 'rt', encoding='utf-8') as my_file:
#     print(sum(map(int, my_file.readlines())))


# from random import randint as random_int
# with open(input(), 'rt', encoding='utf-8') as my_file:
#     list_lines = my_file.readlines()
#     # print(list_lines)
#     print(list_lines[random_int(0, len(list_lines))])


# file = open(input(), 'rt', encoding='utf-8')
# print(file.readlines()[-2])
# file.close()
# # так лучше, файл за областью видимости закрывается
# with open(input()) as output:
#     print(output.readlines()[-2])
#     # конец области видимости.

