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
# 4
a, b = map(int, input().split())
if a <= b:
    print(*[val ** 2 for val in range(a, b + 1)])
else:
    print(*[val ** 3 for val in range(a, b - 1, -1)])