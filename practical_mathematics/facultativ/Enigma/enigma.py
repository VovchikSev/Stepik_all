#
# Энигма https://stepik.org/lesson/283487/step/2?unit=284631 начало
# доп материал https://habr.com/ru/post/217331/
# 4.7 Энигма 1. Реализуйте функцию Ротора шифрования.

# Sample Input 1:
# text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# disk = 0
# Output:
# Encryption (forward): ABCDEFGHIJKLMNOPQRSTUVWXYZ
# Decryption (forward): ABCDEFGHIJKLMNOPQRSTUVWXYZ
#
# Encryption (back): ABCDEFGHIJKLMNOPQRSTUVWXYZ
# Decryption (back): ABCDEFGHIJKLMNOPQRSTUVWXYZ

#    ROTORS = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
#              1: 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
#              2: 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
#              3: 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
#              4: 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
#              5: 'VZBRGITYUPSDNHLXAWMJQOFECK',
#              6: 'JPGVOUMFYQBENHZRDKASXLICTW',
#              7: 'NZJHGRCXMYSWBOUFAIVLPEKQDT',
#              8: 'FKQHTLXOCBJSPDZRAMEWNIUYGV',
#              'beta': 'LEYJVCNIXWPBQMDRTAKZGFUHOS',
#              'gamma': 'FSOKANUERHMBTIYCWLQPZXVGJD'
#             }

# Диски рефлекторов: 0 - без изменений,  1 - reflector B ,  2 - reflector C,  3 - reflector B Dünn,
# 4 - reflector C Dünn.
# REFLECTORS = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
#               1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
#               2: 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
#               3: 'ENKQAUYWJICOPBLMDXZVFTHRGS',
#               4: 'RDOBJNTKVEHMLFCWZAXGYIPSUQ',
#               }


# def rotor(symbol, n, reverse=False):
#     rotors = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
#               1: 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
#               2: 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
#               3: 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
#               }
#     if reverse:
#         return rotors[0][rotors[n].index(symbol)]
#     else:
#         return rotors[n][rotors[0].index(symbol)]


def reflector(symbol, n):
    reflectors = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                  1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
                  2: 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
                  3: 'ENKQAUYWJICOPBLMDXZVFTHRGS',
                  4: 'RDOBJNTKVEHMLFCWZAXGYIPSUQ',
                  }
    return reflectors[0][reflectors[n].index(symbol)]


def rotor(symbol, src_n, dst_n, reverse=False):
    rotors = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
              1: 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
              2: 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
              3: 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
              }
    if reverse:
        return rotors[0][rotors[n].index(symbol)]
    else:
        return rotors[n][rotors[0].index(symbol)]


def enigma(text, ref, rot1, rot2, rot3):
    ret_text = ""
    for ch in text:
        ret_text = ret_text + ""


# последовательность шифрования
# rot3, rot2, rot3, ref, rot1, rot2, rot3
# https://github.com/Xelerezex/learning-space/tree/3d7ff912088c9e602f2becd4522b8b97e7f9c109/stepik-courses/stepik-practice-python-math/03-facultative/4.7-enigma
if __name__ == "__main__":
    print(enigma('A', 1, 1, 2, 3))  # U




