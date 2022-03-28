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
# [print(in_str) for _ in range(in_count)]
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

#  9
# recept_list = []
# for _ in range(int(input())):
#     censure = input()
#     if "соль" not in censure:
#         recept_list.append(censure)
# print(*recept_list, sep=", ")

# 10
# result = 0
# for value in range(50, 101):
#     result += value ** 3
# print(result)

# 11
#  слова длиннее 10 заменить
# result_list = []
# for _ in range(int(input())):
#     censure = input()
#     if len(censure) > 10:
#         result_list.append(censure[0] + str(len(censure) - 2) + censure[-1])
#         pass
#     else:
#         result_list.append(censure)
# print(*result_list, sep="\n")
#  короткое, но малопонятное решение. цикл интересен: for w in [input() for _ in range(int(input()))] можно использовать
# # print("\n".join((w, f'{w[0]}{len(w) - 2}{w[-1]}')[len(w) > 10] for w in [input() for _ in range(int(input()))]))


