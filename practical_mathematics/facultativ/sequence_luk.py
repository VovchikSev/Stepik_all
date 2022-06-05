# Последовательность Люка
# https://stepik.org/lesson/178503/step/1?unit=154906
# Напишите функцию luka(L0, L1, n), которая принимает на вход параметры:
# L0, L1 - 0й и 1й члены последовательности соответственно
# n - номер числа из последовательности, которое необходимо вернуть

def luka(L0, L1, n):
    # L2 = L0 + L1
    res_list = [L0, L1]
    while len(res_list) <= n + 1:
        res_list.append(res_list[-1] + res_list[-2])
    return res_list[n]


from decimal import *
getcontext().prec = 50


def fi(L0, L1, n):
    # res_list = [Decimal(luka(L0, L1, n)), Decimal(luka(L0, L1, n - 1))]
    return Decimal(luka(L0, L1, n)) / Decimal(luka(L0, L1, n - 1))


print(fi(*map(int, input().split())))
