# lst_in = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]]
# l2 = [value for value_list in lst_in for value in value_list]
# print([value
#        for value_list in lst_in[::-1]
#        for value in value_list[::-1]])
# for value_list in lst_in[::-1]:
#     for value in value_list[::-1]:
#         print(value, end=" ")


# in_lst = list(map(int, input().split()))
# len_col = int(len(in_lst) ** .5)
#
# out_lst = [in_lst[index_s * len_col:index_s * len_col + len_col] for index_s in range(len_col)]
# print(*out_lst, sep="\n")

lst_in = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [5, 4, 3]]

row_len = len(lst_in)
col_len = len(lst_in[0])

# t_res = [[in_lst[j][i] for j in range(len(in_lst[i]))] for i in range(len(in_lst))]
# print(t_res)
# for row_ind in range(len(in_lst)):
#     for col_ind in range(len(in_lst[row_ind])):
#         t_res[col_ind][row_ind] = in_lst[row_ind][col_ind]
# [print(*row) for row in t_res]
# print(row_len, col_len)
# [print(*[lst_in[j][i] for j in range(row_len)]) for i in range(col_len)]

# str_in = "вологда=город ho_use=дом True=1 5=отлично 9=божественно"
# # d = dict([i.split('=') for i in input().split()])
# d = dict([value.split("=") for value in str_in.split()])
# print(d)
# print("ДА" if 'house' in d and 'True' in d and '5' in d else "НЕТ")


# lst_in = ['+71234567890 Сергей', '+71234567810 Сергей', '+51234567890 Михаил', '+72134567890 Николай']
#
#
# def intoBinary(number: int) -> str:
#     if not number: return "0"
#     binary_number = ""
#     d = dict(zip([value for value in range(16)],
#                  [str(value) if value < 10 else chr(value + ord("A") - 10)
#                   for value in range(16)]))
#     print(d)
#     while number:
#         binary_number = d[number % 2] + binary_number
#         number = (number - 1) / 2 if number % 2 else number / 2
#
#     return "".join(binary_number)
#
#
# print(intoBinary(int(input())))


# # 6.1 Введение в словари
# # номер_1 имя_1
# # номер_2 имя_2
# # ...
# # номер_N имя_N
# # Необходимо создать словарь d, где ключами будут имена, а значениями - список номеров телефонов для этого имени.
# # Обратите внимание, что одному имени может принадлежать несколько разных номеров.
# # Полученный словарь вывести командой: print(*sorted(d.items()))
# # без ввода готовый список
# lst_in = ['+71234567890 Сергей', '+71234567810 Сергей', '+51234567890 Михаил', '+72134567890 Николай']
# d = {}
# for str_value in lst_in:
#     value, key = str_value.split()
#     d.setdefault(key, []).append(value) # это красивее как мне кажется
#     # d[key] = d.get(key, []) + [value] # не нравится но как вариант можно использовать
# print(*sorted(d.items()))


# Подвиг 9. Пользователь вводит в цикле целые положительные числа, пока не введет число 0.
# Для каждого числа вычисляется квадратный корень (с точностью до сотых) и значение выводится на экран (в столбик).
# С помощью словаря выполните кэширование данных так, чтобы при повторном вводе того же самого числа
# результат не вычислялся, а бралось ранее вычисленное значение из словаря. При этом на экране должно выводиться:
# значение из кэша: <число>

my_dict = {}
my_lst = []
while in_value := int(input()):
    # переделать все в одном цикле и без in_value := не везде понимается
    my_lst.append(in_value)

for value in my_lst:
    if value in my_dict:
        print(f"значение из кэша: {my_dict[value]}")
    else:
        my_dict[value] = round(value ** .5, 2)
        print(my_dict[value])
print(my_lst)
