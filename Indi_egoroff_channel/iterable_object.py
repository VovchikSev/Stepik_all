# 5 Итерируемые объекты и цикл for


# 5.1 Функция range и итерируемые объекты

# 5.2 Цикл for. Обход элементов функции range
# 1
# print(*range(1, int(input()) + 1), sep="\n")
# 2
# print(*range(int(input()) , 0, -1), sep="\n")
# 3
# [ print("Надо было брать биткоин в 2012!") for _ in range(13)]
# 4
# in_str = input()
# in_count = int(input())
# [ print(in_str) for _ in range(in_count)]
# 5
# for value in range(int(input()), int(input()) + 1):
#     if value % 3 == 0 and value % 5 == 0:
#         print("FizzBuzz")
#     else:
#         if value % 3 == 0:
#             print("Fizz")
#         elif value % 5 == 0:
#             print("Buzz")
#         else:
#             print(value)
# 6
# for value in range(int(input()), int(input()) + 1):
#     print(f"Число {value}; его квадрат = {value * value}; его куб = {value ** 3}")
# 7
# mishka_score = cris_score = 0
# for value in range(int(input())):
#     mishka, cris = map(int, input().split())
#     if mishka > cris:
#         mishka_score += 1
#     elif cris > mishka:
#         cris_score += 1
#
# print("Mishka" if mishka_score > cris_score else "Chris" if cris_score > mishka_score else "Friendship is magic!^^")

# 8
# my_list = [input().lower() for _ in range(int(input()))]
# for word in my_list:
#     if "рок" in word:
#         print(my_list.index(word) + 1, word.find("рок") + 1)
# print(my_list)

