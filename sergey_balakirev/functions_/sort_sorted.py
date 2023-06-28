

"""
Подвиг 2. На вход поступает список целых чисел, записанных в одну строчку через пробел. Преобразуйте сначала эту строку
в список из целых чисел, а затем список в кортеж из целых чисел. То есть, в программе будет две разные коллекции:
список и кортеж. Отсортируйте по возрастанию значений эти коллекции методом sort, если это возможно, а иначе - примените
функцию sorted.
На экран ничего выводить не нужно, только сформировать две отсортированные коллекции: lst (список)
- результат сортировки списка; tp_lst (кортеж) - результат сортировки кортежа.
P.S. На результаты сортировок обязательно должны ссылаться переменные с именами lst и tp_lst!
Sample Input: -2 -1 8 11 4 5
Sample Output: True
"""

# lst = sorted(list(map(int, input().split())))
# tp_lst = tuple(lst)
# print(lst)
# print(tp_lst)


"""
Подвиг 3. На вход функции с именем get_sort поступает словарь, например, такой:
d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}
Необходимо отсортировать словарь d по убыванию ключей (лексикографическая сортировка строк) и возвратить список из
соответствующих значений ключей словаря. Например, для указанного словаря d, результатом должен быть список:
['дерево', 'лошадь', 'собака', 'кот', 'книга']
Сигнатура функции get_sort должна быть следующей:
def get_sort(d): ...
В программе только определить функцию, вызывать ее не нужно и что-либо выводить на экран тоже не нужно.
P. S. Подсказка: список в функции get_sort лучше всего формировать с помощью генератора списков.
Sample Input:
Sample Output:
True
"""

# def get_sort(d):
#     return list(map(lambda x:x[1], sorted(d.items(), reverse=True)))
#     print(d)
#
#
# d_in = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}
# print(get_sort(d_in))

"""
Подвиг 4. На вход программы поступает список целых чисел, записанных в одну строчку через пробел. Необходимо выбрать из
них четыре наибольших уникальных значения. Результат вывести на экран в порядке их убывания в одну строчку через пробел.
Sample Input:  10 5 4 -3 2 0 5 10 3
Sample Output: 10 5 4 3
"""

# # in_list = [int(value)  for value in input().split()]
# print(*sorted(list(set( [int(value)  for value in input().split()])), reverse=True)[:4])

"""
Подвиг 5. На вход программы поступают два списка целых чисел (каждый в отдельной строке), записанных в одну строчку
через пробел. Длины списков могут быть разными. Необходимо первый список отсортировать по возрастанию, а второй - по
убыванию. Полученные пары из обоих списков сложить друг с другом и получить новый список чисел. Результат вывести на
экран в виде строки чисел через пробел.
P. S. Подсказка: не забываем про функцию zip.
Sample Input:
7 6 4 2 6 7 9 10 4
-4 5 10 4 5 65
Sample Output: 67 14 9 11 10 3
"""
# in_lst1 = sorted(list(map(int, input().split())))
# in_lst2 = sorted( list(map(int, input().split())), reverse=True)
# print(in_lst1)
# print(in_lst2)
# res = [x + y for x, y in zip(in_lst1, in_lst2)]
# print(*res)
# # все это в одну строку
# # print(*[sum([x, y]) for x, y in zip(sorted(list(map(int, input().split()))), sorted( list(map(int, input().split())), reverse=True))])

"""
Подвиг 6. На вход программы поступает список товаров в формате:

название_1:цена_1
...
название_N:цена_N

Необходимо преобразовать этот список в словарь, ключами которого выступают цены (целые числа), а значениями -
соответствующие названия товаров. Необходимо написать функцию, которая бы принимала на входе словарь и возвращала список
из наименований трех наиболее дешевых товаров.
Вызовите эту функцию и отобразите на экране полученный список в порядке возрастания цены в одну строчку через пробел.
P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
Sample Input:
смартфон:120000
яблоко:2
сумка:560
брюки:2500
линейка:10
бумага:500
Sample Output: яблоко линейка бумага
"""
lst_in = ['смартфон:120000', 'яблоко:2', 'сумка:560', 'брюки:2500', 'линейка:10', 'бумага:500']

my_dict = {int(value): key for key, value in (line.split(":") for line in lst_in)}
# print(my_dict)
# print(sorted(my_dict)[:3])
for key in sorted(my_dict)[:3]:
    print(my_dict[key], end=" ")