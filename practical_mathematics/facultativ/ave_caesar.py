

# Программа должна циклически сдвинуть данный набор чисел на nn шагов и вывести полученный результат,
# разделяя числа символом пробела. Если nn является положительным числом,
# сдвиг происходит вправо, если отрицательным — влево.

# 1 2 3 4 5
# -2
# 3 4 5 1 2

# 1 2 3 4 5
# 1
# 5 1 2 3 4

# def name(alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
#     pass
#
#
# in_list = list(map(int, input().split()))
# shift = int(input())
#
# negative = -1 if shift < 0 else 1
# if abs(shift) > len(in_list):
#     # сдвиг больше длинны массива
#     shift = abs(shift) % len(in_list) * negative
#
# print(in_list, shift)
#
# if shift > 0:
#     print(*in_list[-shift:] + in_list[:-shift])
# elif shift < 0:
#     print(*in_list[-shift:] + in_list[:-shift])
# else:
#     print(*in_list)


def caesar(text: str, key: int) -> str:
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if abs(key) > len(alphabet):
        key = abs(key) % len(alphabet) * (-1 if key < 0 else 1)
    prepared_text = "".join(filter(lambda x: x in alphabet, text.upper()))
    crypted_alphabet = alphabet[key:] + alphabet[:key]

    result_str = ""
    for ch in prepared_text:
        result_str = result_str + crypted_alphabet[alphabet.index(ch)]
    return result_str


shift = 42
message = "In cryptography, a Caesar cipher"

print(caesar(text=message, key=shift))
#-3
# YDSHOFJEWHQFXOQSQUIQHSYFXUHQBIEADEMDQISQUIQHISYFXUHJXUIXYVJSYFXUHSQUIQHISETUEHSQUIQHIXYVJYIEDUEVJXUIYCFBUIJ
# INCRYPTOGRAPHYACAESARCIPHERALSOKNOWNASCAESARSCIPHERTHESHIFTCIPHERCAESARSCODEORCAESARSHIFTISONEOFTHESIMPLESTANDMOSTWID
