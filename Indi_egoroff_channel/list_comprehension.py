# 5.9 Генераторы списков Python | List comprehension
# 1
# zeroes = [0] * 100
# print(zeroes)

# 2
# my_list =[val for val in range(1, int(input())+1)]
# print(my_list)

# 3
# in_value = int(input())
# my_list = [val for val in range(1, in_value + 1) if in_value % val == 0]
# print(my_list)
#
# 4
# in_value = int(input())
# my_list = [val for val in range(in_value, in_value * in_value + 1) if bool(val % 2)]
# print(my_list)
#
# 4 [j for i in list for j in i]
# vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
# short_list = [val for val_array in vector for val in val_array]
# print(short_list)

