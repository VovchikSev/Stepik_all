# Последовательность Люка
# https://stepik.org/lesson/178503/step/1?unit=154906
# Напишите функцию luka(L0, L1, n), которая принимает на вход параметры:
# L0, L1 - 0й и 1й члены последовательности соответственно
# n - номер числа из последовательности, которое необходимо вернуть

# def luka(L0, L1, n):
#     for i in range(n):
#         L1, L0 = L0 + L1, L1
#     return L0


# from decimal import *
# getcontext().prec = 50
#
#
# def fi(L0, L1, n):
#     for i in range(2, n+1):
#         L0, L1 = L1, L0 + L1
#     return Decimal(L1) / Decimal(L0)
#
#
# print(fi(*map(int, input().split())))

def super_L(n):

    n0, n1 = 2, 1
    for _ in range(2, n + 1):
        n0, n1 = n1, n1 + n0
    return n1


print(super_L(1200))


