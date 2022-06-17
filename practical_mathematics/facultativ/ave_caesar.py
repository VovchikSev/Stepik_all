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
#      return result_str
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

# from random import shuffle
#
#
# def disc_generator(alphabet: str) -> str:
#     alphabet = list(alphabet)
#     shuffle(alphabet)
#     return "".join(alphabet)
#
#
# print(disc_generator(input()))


#  Цилиндр Джеферсона - это механический шифровальный аппарат, который состоит из нескольких дисков,
#  на которых записаны алфавиты (состоящие из одинаковых символов, но в случайном порядке).
#
# Для шифрования с его помощью текст разбивают на блоки, длина каждого блока равна числу дисков в механизме.
#
# Каждый символ блока шифруется с помощью алгоритма Цезаря с использованием соответствующего диска
# (т.е. 1й символ с помощью 1 диска, 2й символ с помощью 2 диска и т.д.) с общим сдвигом.
#
# Таким образом сдвиг (ключ для шифрования Цезаря) не является секретом для цилиндра Джеферсона -
# цилиндры легко повернуть вокруг оси и на них видны сразу все комбинации расшифровки, так что даже не требуется
# брутфорс. Однако, если сами цилиндры (а значит и порядок символов в алфавитах) хранятся в секрете,
# а так же в секрете порядок следования алфавитов, то такой метод шифрования очень надёжен.
#
# Переменная clear_alphabet содержит исходный алфавит
# Переменная n содержит число
# Создайте n новых алфавитов и поместите список из них в переменную discs.
# Создайте функцию jefferson_encryption(text, discs, step, reverse=False), реализующую "цилиндр Джеферсона"
#
# text - исходный текст
# discs - список из словарей (строк)
# step - сдвиг на которых смещаются символы с помощью алгоритма Цезаря (ключ шифрования для шифра Цезаря)
# reverse - признак расшифровки, если находится в значении True, это значит, что функцию надо использовать
# для расшифровки текста, т.к. каждый сдвиг должен быть отрицательным. (по умолчанию False)

# пример ввода

# from random import shuffle
#
#
# def disc_generator(alphabet: str) -> str:
#     ret_l = list(alphabet)
#     shuffle(ret_l)
#     return "".join(ret_l)
#
#
# clear_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# n = 6
# text = "Some encrypted text"
# disks = [disc_generator(clear_alphabet) for _ in range(n)]
#
#
# def jefferson_encryption(text, discs, step, reverse=False):
#     print(clear_alphabet)
#
# print(disks)

######################################################
# https://github.com/Igor999/Encryption-of-a-cylinder-of-Jefferson/blob/master/Jefferson.py
######################################################
# import random
# n = 6
# clear_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# discs = []
# random.seed(42)
# for i in range(n):
#     alph = list(map(str, clear_alphabet))
#     random.shuffle(alph)
#     discs.append(alph)
# d = []
# rows = ""
# for i in discs:
#     for o in i:
#         rows += o
#     d.append(rows)
#     rows = ""
# discs = d
# #print("DISCS:")
# #for i in discs:
# #    print(i)
# #print()
#
#
# def jefferson_encryption(text, discs, step, reverse=False):
#     text = text.upper()
#     new_text = ""
#     for current_disk in text:
#         if current_disk in clear_alphabet:
#             new_text += current_disk
#     k = 0
#     result = ""
#     for t in new_text:
#         current_disk = discs[k].index(t)
#         if reverse:
#             current_disk = (current_disk - step) % len(clear_alphabet)
#         else:
#             current_disk = (current_disk + step) % len(clear_alphabet)
#
#         result +=discs[k][current_disk]
#         k += 1
#         if k > (n-1):
#             k = 0
#     return result
#####################################################
def kidds_encryption(text, reverse=False):
    letter = ['e', 't', 'h', 'o', 's', 'n', 'a', 'i', 'r', 'f', 'd', 'l', 'm', 'b', 'y', 'g', 'u', 'v', 'c', 'p']
    symbols = ['8', ';', '4', '‡', ')', '*', '5', '6', '(', '1', '†', '0', '9', '2', ':', '3', '?', '¶', '-', '.']
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet = alphabet.lower()
    new_text = ""
    result = ""
    if reverse:
        for i in text:
            ind = symbols.index(i)
            result += letter[ind]
    else:
        text = text.lower()
        for i in text:
            if i in alphabet:
                new_text += i
        for i in new_text:
            if i in letter:
                ind = letter.index(i)
                result += symbols[ind]
            else:
                result += ""
    return result
