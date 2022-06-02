

# def numerics(n):
#     return list(map(int, str(n)))
#
#
# print(numerics(4224))


def kaprekar_step(L):
    L.sort()
    return int("".join(map(str, L[::-1]))) - int("".join(map(str, L)))


print(kaprekar_step([6, 8, 0, 4]))

# в порядке увеличения цифр в исходном списке
# в порядке уменьшения цифр в исходном списке
# Вычесть из большего числа меньшее и вернуть результат.
