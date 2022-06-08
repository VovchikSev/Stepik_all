
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
#
#
# print(kaprekar(218400870420))


# https://stepik.org/lesson/180027/step/5?unit=154907


def convert(num, to_base=10, from_base=10):

    if type(num) == int:
        pass
    elif type(num) == str:
        pass

