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
orig_str = list(input())
bad_str = list(input())
find_char = ""
for ch in bad_str:
    if ch not in orig_str:
        find_char = ch
        break

if find_char == "":
    for index in range(len(orig_str)):
        if orig_str[index] != bad_str[index]:
            find_char = bad_str[index]
            break
print(find_char if find_char != "" else bad_str[-1])
# print(orig_str)
# print(bad_str)
