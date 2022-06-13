
# https://stepik.org/lesson/180027/step/1?unit=154907

# def kaprekar(n):
#     qadre = n ** 2
#     qadre_str = str(qadre)
#     for value in range(1, len(qadre_str)):
#
#         if n == (int(qadre_str[:value]) + int(qadre_str[value:])):
#             print(f"{qadre_str[:value]} + {qadre_str[value:]} = {int(qadre_str[:value]) + int(qadre_str[value:])}")
#             return True
#     return False


# print(kaprekar(218400870420))


# https://stepik.org/lesson/180027/step/5?unit=154907


def convert(num, to_base=10, from_base=10):
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)

    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert(n // to_base, to_base) + alphabet[n % to_base]


def kaprekar(n, base=10) -> bool:

    def kaprekar_10(in_value: int) -> bool:
        qadre = in_value ** 2
        qadre_str = str(qadre)
        for value in range(1, len(qadre_str)):
            left_value = int(qadre_str[:value])
            right_value = int(qadre_str[value:])
            if right_value != 0 and n == (left_value + right_value):
                # print(f"{qadre_str[:value]} + {qadre_str[value:]} = {int(qadre_str[:value]) + int(qadre_str[value:])}")
                return True
        return False

    if isinstance(n, str):
        n = int(n, base)
    if base == 10:
        return kaprekar_10(n)

    n_q = convert(n ** 2, to_base=base)
    for value in range(1, len(n_q)):
        left_value = int(n_q[:value], base)
        right_value = int(n_q[value:], base)
        # print(right_value != 0, right_value)
        if right_value != 0 and left_value + right_value == n:
            return True
            # print(f"{n_q[:value]} +++ {n_q[value:], base} = {int(n_q[:value], base) + int(n_q[value:], base)}")
    return False


"""
Сделал очень просто:
1 функция - convert(num, to_base=10, from_base=10): из предыдущего задания
2 фукнция - kaprekar_10(n): вызывается если размерность 10
3 функция - kaprekar(n, base=10): (перевожу в 10 систему счисления, int, возвожу в квадрат, 
перевожу обратно в base в виде строки и пускаю по циклу) 
(в цикле проверка num == int() + int() от кусков переведенных чисел, 
используя convert(,from_base=base))

"""

test_1 = [9, 45, 55, '99', '297', 703, 999, '2223', 2728, '4879']
test_2 = [10, 46, 56, 100, 298, 704, '1000', '2224', '2729', '4880']
test_3 = ['6', 'A', 'F', '33', '55', '5B', '78', '88', 'AB', 'CD', 'FF', '15F', '334', '38E']

print([kaprekar(i) for i in test_1]) # Тест чисел Капрекара из системы с основанием 10

print([kaprekar(i) for i in test_2 ]) # Тест НЕ чисел Капрекара из системы с основанием 10

print([kaprekar(i, base=16) for i in test_3]) #Тест чисел Капрекара из системы с основанием 16
