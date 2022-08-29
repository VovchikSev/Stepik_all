
# in_str = '8 11 -5 -2 8 11 -5'
# in_list = [int(value) for value in input().split()]
# my_tuple = ()

# for value in in_list:
#     if not value in my_tuple:
#         my_tuple = my_tuple + (value,)

# print(*my_tuple)

"""
Подвиг 8. Вводятся целые числа в одну строку через пробел. На их основе формируется кортеж. 
Необходимо найти и вывести все индексы неуникальных (повторяющихся) значений в этом кортеже. 
Результат отобразите в виде строки чисел, записанных через пробел.
"""
# in_str = "5 4 -3 2 4 5 10 11"

# my_tuple = tuple(int(value) for value in in_str.split())
# # my_tuple = tuple(int(value) for value in input().split())

# for index in range(len(my_tuple)):
#     if my_tuple.count(my_tuple[index]) > 1:
#         print(index, end=" ")

    

# print(my_tuple)

