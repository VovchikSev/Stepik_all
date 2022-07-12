# https://stepik.org/lesson/283487/step/2?unit=284631
# мое решение

def rotor(symbol, n, reverse=False):
    rotors = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
              1: 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
              2: 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
              3: 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
              }
    if reverse:
        return rotors[0][rotors[n].index(symbol)]
    else:
        return rotors[n][rotors[0].index(symbol)]


if __name__ == "__main__":
    pass
