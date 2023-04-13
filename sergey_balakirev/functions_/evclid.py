
def get_nod(a:int, b:int)->int:
    """
    Вычисляется НОД для натуральных чисел a и b по алгоритму Евклида

    Args:
        a (int): Первое натуральное число
        b (int): Второе натуральное число
    return НОД
    """
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b
    return a



def test_nod(func:function):
    pass


res = get_nod(18, 24)
print(res)

