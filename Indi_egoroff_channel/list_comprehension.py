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
"""
Если a<=b необходимо сформировать список квадратов целых чисел на интервале от а до b включительно и вывести его на экран.
Если же a>b, необходимо сформировать список кубов целых чисел на интервале от a до b включительно,
двигаясь в порядке убывания, и затем вывести его.
"""
a, b = map(int, input().split())
if a <= b:
    print(*[val ** 2 for val in range(a, b + 1)])
else:
    print(*[val ** 3 for val in range(a, b - 1, -1)])
