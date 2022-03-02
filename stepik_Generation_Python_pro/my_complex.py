
n, z1, z2  = int(input()), complex(input()), complex(input())
print(z1 ** n + z2 ** n + z1.conjugate() ** n + z2.conjugate() ** (n + 1))

# numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j,
#            -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
# max_mod = 0
# for val in range(len(numbers)):
#     if abs(numbers[val]) > abs(numbers[max_mod]):
#         max_mod = val
# print(numbers[max_mod])
# print(abs(numbers[max_mod]))


# in_str1 = input()
# in_str2 = input()
# print(f'({in_str1}) + ({in_str2}) =', complex(in_str1) + complex(in_str2))
# print(f'({in_str1}) - ({in_str2}) =', complex(in_str1) - complex(in_str2))
# print(f'({in_str1}) * ({in_str2}) =', complex(in_str1) * complex(in_str2))