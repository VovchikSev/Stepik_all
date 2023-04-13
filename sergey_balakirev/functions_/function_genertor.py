# пример из теории
# def get_list():
#     for x in range(1, 10):
#         result = range(x, 11)
#         yield sum(result) / len(result)
#
#
# a = get_list()
# print(list(a))


"""
Подвиг 1. Вводится натуральное число N. Необходимо определить функцию-генератор с именем get_sum, которая бы
возвращала текущую сумму чисел последовательности длины N в диапазоне целых чисел [1; N]. Например:
- для первого числа 1 сумма равна 1;
- для второго числа 2 сумма равна 1+2 = 3
....
- для N-го числа сумма равна 1+2+...+(N-1)+N
Реализовать функцию-генератор get_sum без использования коллекций. Вызывать ее не нужно, только определить.
Sample Input: 5
Sample Output: 1 3 6 10 15
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

N = int(input())


def get_sum(number):
    counter = 1
    numbers = [counter]
    
    while counter <= number:
        yield sum(numbers)
        counter += 1
        numbers.append(counter)


a = get_sum(N)
for val in a:
    print(val)

