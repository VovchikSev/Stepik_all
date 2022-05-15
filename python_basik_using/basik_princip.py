
# https://stepik.org/lesson/24460/step/10?unit=6766
"""
9
add global a
create foo global
add foo b
get foo a
get foo c
create bar foo
add bar a
get bar a
get bar b

Sample Output:
global
None
bar
foo
"""
# in_count = int(input())
# my_dict = {"global": ["", set()]}
#
#
# def get_value(ns: str, narg: str) -> str:
#     result = None
#     # проверить есть ли в my_dict[ns]
#     if ns in my_dict.keys():
#         parent, values_set = my_dict[ns]
#         if narg in values_set:
#             result = ns  # искомое имя в текущем пространстве.
#         else:
#             while parent != "":
#                 if parent in my_dict.keys():
#                     parent_n, values_set = my_dict[parent]
#                     if narg in values_set:
#                         result = parent
#                         break
#                     else:
#                         parent = parent_n
#     return result
#
#
# for _ in range(in_count):
#     cmd, name_sp, arg = input().split()
#     if cmd == "add":
#         # добавить переменную в namespace
#         tm_list = my_dict[name_sp]
#         tm_list[1].add(arg)
#         my_dict[name_sp] = tm_list
#
#     elif cmd == "create":
#         # создать namespace в arg
#         my_dict[name_sp] = [arg, set()]
#
#     elif cmd == "get":
#         # получить переменную arg из name_sp
#         print(get_value(name_sp, arg))
#
# print(my_dict)

# https://stepik.org/lesson/24461/step/9?unit=6767
class Buffer:
    def __init__(self):
        self.buffer = []


    def add(self, *a):
        self.buffer += a
        last_index = -5 if len()
        self.in_list = self.buffer[-1]
        # добавить следующую часть последовательности


    def get_current_part(self):
        return self.in_list
        # вернуть сохраненные в текущий момент элементы последовательности
        # в порядке, в котором они были добавлены


buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]