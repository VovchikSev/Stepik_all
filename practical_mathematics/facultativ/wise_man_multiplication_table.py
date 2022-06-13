
# таблица умножения мудреца
# 96x97
# 9312

# def simple_multiplication(x, y):
#     return ((100 - ((100 - x) + (100 - y))) * 100) + (100 - x) * (100 - y)
#
#
# def simple_multiplication_bad(x, y):
#     first_num = 100 * (100 - ((100 - x) + (100 - y)))
#     second_num = (100 - x) * (100 - y)
#     return int(str(first_num) + str(second_num))
#
#
# def multiplication_check(x, y) -> bool :
#     return x * y == simple_multiplication(x, y)
#
#
# def multiplication_check_list(start=10, stop=99):
#     bad_count = 0
#     ok_count = 0
#     for x_ in range(start, stop + 1):
#         for y_ in range (start, stop + 1):
#             if multiplication_check(x_, y_):
#                 ok_count += 1
#             else:
#                 bad_count += 1
#     print(f"Правильных результатов: {ok_count}")
#     print(f"Неправильных результатов: {bad_count}")


"""
Напишите функцию wisdom_multiplication(x, y, length_check = True), 
реализующую умножение по схеме мудреца с прошлого шага.
1 Вычитаем из 100 первое и второе число.
2 Складываем результаты шага 1.
3 Вычитаем из 100 результат шага 2.
4 Перемножаем результаты шага 1.
5 Результат шага 3 даёт первые цифры результата, а результат шага 4 даёт последние 2 цифры результата.
В зависимости от значения аргумента length_check функция проверяет или нет длину результата шага 4 
и при необходимости дописывает 0 перед ним (если результат всего 1 цифра).
"""


# def wisdom_multiplication(x, y, length_check=True) -> int:
#     x_100, y_100 = 100 - x, 100 - y
#     step_3 = str(100 - (x_100 + y_100))
#     step_4 = str(x_100 * y_100)
#     if length_check and len(step_4) == 1:
#         step_4 = "0" + step_4
#     return int(step_3 + step_4)


def wisdom_multiplication(x, y, length_check=True) -> bool:
    x_100, y_100 = 100 - x, 100 - y
    step_3 = str(100 - (x_100 + y_100))
    step_4 = str(x_100 * y_100)
    if length_check and len(step_4) == 1:
        step_4 = "0" + step_4
    return int(step_3 + step_4) == x * y


def multiplication_check_list(start=10, stop=99, length_check=True):
    bad_count = 0
    ok_count = 0
    for x_ in range(start, stop + 1):
        for y_ in range(start, stop + 1):
            if wisdom_multiplication(x_, y_, length_check):
                ok_count += 1
            else:
                bad_count += 1
    print(f"Правильных результатов: {ok_count}")
    print(f"Неправильных результатов: {bad_count}")


x1, y1 = 98, 99
print(multiplication_check_list(x1, y1, length_check=True))
