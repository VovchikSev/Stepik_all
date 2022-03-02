from fractions import Fraction


# frac_set = set()
# for i in range(1, int(input()) + 1):
#     for j in range(1, i):
#         frac_set.add(Fraction(j, i))
# for val in sorted(frac_set):
#     print(val)


# in_value = int(input())
# full_list = [val for val in range(1, in_value)]
#
# result = ""
# for index in range(len(full_list)):
#     for idx in range(len(full_list) ):
#
#         if full_list[index] < full_list[idx] and math.gcd(full_list[index], full_list[idx]) == 1:
#             print(f"{full_list[index]}/{full_list[idx]}")
#             # result = f"{full_list[index]}/{full_list[idx]}"
# print(result)

# from math import factorial
# print(sum([Fraction(1, math.factorial(i)) for i in range(1, int(input()) + 1)]))


# result = Fraction(0, 1)
# index = 0
# for _ in range(int(input())):
#     index += 1
#     result += Fraction(Fraction(1), Fraction(index ** 2))
# print(result)
# аналог всего в пару строк, где первая строка подключение библиотеки.
# from fractions import Fraction as F
# print(sum([F(1, i**2) for i in range(1, int(input()) + 1)]))
#  вычисление времени исполнения
# import time
# start_time = time.time()
# # наш код
# print("--- %s seconds ---" % (time.time() - start_time))


# in_1 = input()
# in_2 = input()
# tmp1 = [int(val) for val in in_1.split("/")]
# tmp2 = [int(val) for val in in_2.split("/")]
# first = Fraction(tmp1[0], tmp1[1])
# second = Fraction(tmp2[0], tmp2[1])
#
# print(f'{in_1} + {in_2} = {first + second}')
# print(f'{in_1} - {in_2} = {first - second}')
# print(f'{in_1} * {in_2} = {first * second}')
# print(f'{in_1} / {in_2} = {first / second}')


# s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'
#
# list_fr = [Fraction(st) for st in s.split()]
# print(max(list_fr) + min(list_fr))

# numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14', '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02', '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31', '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']
#
# for num in numbers:
#     print(f'{num} = {Fraction(num)}')


# from fractions import Fraction
#
# num1 = Fraction(3, 4)     # 3 - числитель, 4 - знаменатель
# num2 = Fraction('0.55')
# num3 = Fraction('1/9')
#
# print(num1, num2, num3, sep='\n')