# 7 Функции
#
# 7.1 Определение и вызов функции. Инструкция def

# def summa_n(n: int):
#     # return sum([value for value in range(1, n + 1)])
#     print(f"Я знаю, что сумма чисел от 1 до {n} равна {sum([value for value in range(1, n + 1)])}")
#
# summa_n(int(input()))
#  3
# def check_password(password: str):
#     count_upper = 0
#     count_digit = 0
#     count_spec = 0
#
#     for ch in password:
#         if ch.isdigit():
#             count_digit += 1
#         if ch.isupper():
#             count_upper += 1
#         if ch in "!@#$%*":
#             count_spec += 1
#     print("Perfect password" if all([len(password), count_digit > 3, count_upper > 0 and count_spec > 0]) else "Easy peasy")


def count_letters(in_str: str):
    count_upper = 0
    count_lower = 0
    for ch in in_str:
        if ch.isalpha():
            print(f"IsAlpha({ch})")
            if ch.lower():
                print(f"islower({ch})")
                count_lower += 1
            else:
                print(f"isupper({ch})")
                count_upper += 1

    print(f"Количество заглавных символов: {count_upper}")
    print(f"Количество строчных символов: {count_lower}")


count_letters("Привет, Старина")
count_letters("QWERTY")
