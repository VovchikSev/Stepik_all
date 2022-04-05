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
phrase = 'Take only the words that start with t in this sentence'
my_list = []
for word in phrase.split():
    if word[0].lower() == "t":
        my_list.append(word)
print(my_list)

