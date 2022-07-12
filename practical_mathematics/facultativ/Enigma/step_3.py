
# https://stepik.org/lesson/283487/step/3?unit=284631
# мой вариант

def reflector(symbol, n):
    reflectors = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                  1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
                  2: 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
                  3: 'ENKQAUYWJICOPBLMDXZVFTHRGS',
                  4: 'RDOBJNTKVEHMLFCWZAXGYIPSUQ',
                  }
    return reflectors[0][reflectors[n].index(symbol)]


if __name__ == "__main__":
    pass
