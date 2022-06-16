
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


# def caesar(text: str, key: int, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
#     # alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     if abs(key) > len(alphabet):
#         key = abs(key) % len(alphabet) * (-1 if key < 0 else 1)
#     prepared_text = "".join(filter(lambda x: x in alphabet, text.upper()))
#     crypted_alphabet = alphabet[key:] + alphabet[:key]
#
#     result_str = ""
#     for ch in prepared_text:
#         result_str = result_str + crypted_alphabet[alphabet.index(ch)]
#     return result_str
#
#
# def bruteforce(text, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
#     len_count = len(alphabet)
#     for index in range(-1, -len_count, -1):
#         print(alphabet[index])
#         print(caesar(text, index, alphabet))
####################################################################
# def get_offset_char(text: str, offset: int, alphabet :str) -> str:
#     crypt_alphabet = alphabet[offset:] + alphabet[:offset]
#     return crypt_alphabet[alphabet.index(text)]
#
#
# def jarriquez_encryption(text, key, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', reverse=False) -> bool:
#     keys = str(key)  # list(map(int, str(key)))
#     keys = keys * (len(text) // len(keys) + 1)
#     prepared_text = "".join(filter(lambda x: x in alphabet, text.upper()))
#     result = ""
#     for index in range(len(prepared_text)):
#         offset = - int(keys[index]) if reverse else int(keys[index])
#         result = result + get_offset_char(prepared_text[index], offset, alphabet)
#     if "АЛМАЗ" in result and "ДАКОСТА" in result:
#         print(key)
#         print(result)
#         return True
#     return False

# ТЛБЛДУЭППТКЛФЧУВНУПБКЗИХТЛТТЫХНЛОИНУВЖММИНПФНПШОКЧЛЕРНТФНАХЖИДМЯКЛТУБЖИУЕЖЕАХЛГЩЕЕ
# ЪУВНГАХИЯШПЙАОЦЦПВТЛБФТТИИНДИДНЧЮОНЯОФВТЕАТФУШБЛРЮЮЧЖДРУУШГЕХУРПЧЕУВАЭУОЙБДБНОЛСКЦБ
# САОЦЦПВИШЮТППЦЧНЖОИНШВРЗЕЗКЗСБЮНЙРКПСЪЖФФШНЦЗРСЭШЦПЖСЙНГЭФФВЫМЖИЛРОЩСЗЮЙФШФДЖО
# ИЗТРМООЙБНФГОЩЧФЖООКОФВЙСЭФЖУЬХИСЦЖГИЪЖДШПРМЖПУПГЦНВКБНРЕКИБШМЦХЙИАМФЛУЬЙИСЗРТЕС
# Постарайтесь расшифровать текст, сделав несколько предположений:
# Текст зашифрован шифром Вижинера (вы его реализовали в предыдущей задаче)
# Ключ вряд ли представляет из себя 2-3 значное число (это было бы слишком легко), но из соображений гуманности
# можно не проверять числа более 6 знаков длиной
# В шифрованном тесте есть все символы алфавита (т.е. словарь можно составить с помощью текста шифровки)
# Расшифрованный текст содержит ряд ключевых слов из произведения (почти наверняка там есть слово "алмаз"
# или фамилия обвиняемого - "Дакоста".
# Хотя текст разбит на строки, на самом деле это не значит, что конец строки приходится на конец слова.

# in_text = "ТЛБЛДУЭППТКЛФЧУВНУПБКЗИХТЛТТЫХНЛОИНУВЖММИНПФНПШОКЧЛЕРНТФНАХЖИДМЯКЛТУБЖИУЕЖЕАХЛГЩЕЕЪУВНГАХИЯШПЙАОЦЦПВТЛБФТТИИНДИДНЧЮОНЯОФВТЕАТФУШБЛРЮЮЧЖДРУУШГЕХУРПЧЕУВАЭУОЙБДБНОЛСКЦБСАОЦЦПВИШЮТППЦЧНЖОИНШВРЗЕЗКЗСБЮНЙРКПСЪЖФФШНЦЗРСЭШЦПЖСЙНГЭФФВЫМЖИЛРОЩСЗЮЙФШФДЖОИЗТРМООЙБНФГОЩЧФЖООКОФВЙСЭФЖУЬХИСЦЖГИЪЖДШПРМЖПУПГЦНВКБНРЕКИБШМЦХЙИАМФЛУЬЙИСЗРТЕС"
#
# import time
# alphabet = "".join(sorted(set(in_text)))
# print(alphabet, len(alphabet))
# start = time.time()
# for index in range(10000, 10 ** 6):
#     if jarriquez_encryption(in_text, index, alphabet, reverse=True):
#         print(f"{time.time() - start:>.4f}")
#         break
import random
from random import shuffle
alphabet = random.shuffle( input())
print(alphabet)


