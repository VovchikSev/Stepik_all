"""
Подвиг 5. 
Вводится список целых чисел в одну строчку через пробел. С помощью словаря выделите только уникальные (не повторяющиеся) 
введенные значения и, затем, сформируйте список из уникальных чисел. Выведите его на экран в виде набора чисел, 
записанных через пробел.
P. S. Такая задача, обычно решается через множества, но мы их еще не проходили, поэтому воспользуемся словарем.
Sample Input:
8 11 -4 5 2 11 4 8
Sample Output:
8 11 -4 5 2 4
"""

# lst_in = list(map(int, input().split()))
# res_dict = {}

# for value in lst_in:
#     if not value in res_dict.keys():
#         res_dict[value] = value

# print(*res_dict.keys())

"""
Дни рождений и имена могут повторяться. На их основе сформировать словарь и вывести его в формате (см. пример ниже):
Sample Input:
3 Сергей
5 Николай
4 Елена
7 Владимир
5 Юлия
4 Светлана
Sample Output:
3: Сергей
5: Николай, Юлия
4: Елена, Светлана
7: Владимир
"""

# import sys
# # считывание списка из входного потока
# lst_in = ['3 Сергей', '5 Николай', '4 Елена', '7 Владимир', '5 Юлия', '4 Светлана']

# my_dict = {}
# for val in lst_in:
#     key, value = val.split()
#     my_dict.setdefault(int(key), [])
#     my_dict[int(key)].append(value)

# for key, value in my_dict.items():
#     print(key, end=": ")
#     print(*value, sep=", ")


"""
Подвиг 7. 
Сергей собирается в поход и готов взвалить на свои хрупкие плечи максимальный вес в N кг (вводится с клавиатуры). 
Он решил класть в рюкзак предметы в порядке убывания их веса (сначала самые тяжелые, затем, все более легкие) так, 
чтобы их суммарный вес не превысил значения N кг. Все предметы даны в единственном экземпляре. 
Выведите список предметов (в строчку через пробел), которые берет с собой Сергей в порядке убывания их веса.
"""
things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300, 
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}


max_weight = int(input())
