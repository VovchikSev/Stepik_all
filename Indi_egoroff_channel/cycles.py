
"""doc."""

# 3  Условия и циклы

# 3.1 Условный оператор
# my_value = int(input())
# print(my_value * 0.87 if my_value < 20000 else my_value)

# list_numbers = input()
# result = 0
# for value in range(1, int(input()) + 1):
#     if not bool(value % 2):
#         result += value
#     else:
#         result -= value

my_value = int(input())
print(round(my_value / 2) if my_value % 2 == 0 else -round((my_value + 1) / 2))
