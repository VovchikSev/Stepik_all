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
# class Buffer:
#     def __init__(self):
#         self.buffer = []
#
#     def add(self, *a):
#         for value in a:
#             # print(value)
#             self.buffer.append(value)
#             # print(self.buffer)
#             if len(self.buffer) == 5:
#                 print(sum(self.buffer))
#                 self.buffer = []
#
#     def get_current_part(self):
#         return self.buffer
#
#
# buf = Buffer()
# buf.add(1, 2, 3)
# buf.get_current_part()  # вернуть [1, 2, 3]
# buf.add(4, 5, 6)  # print(15) – вывод суммы первой пятерки элементов
# buf.get_current_part()  # вернуть [6]
# buf.add(7, 8, 9, 10)  # print(40) – вывод суммы второй пятерки элементов
# buf.get_current_part()  # вернуть []
# buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # print(5), print(5) – вывод сумм третьей и четвертой пятерки
# buf.get_current_part()  # вернуть [1]

# class_structure = {}
# for _ in range(int(input())):
#     in_list = input().split()
#     ancestors = []
#     a_name = in_list[0]
#     if len(in_list) > 0:
#         ancestors = in_list[2:]
#     t_set = class_structure.get(a_name, set([a_name]))
#     t_set = t_set.union(set(ancestors))
#     class_structure[a_name] = t_set
#
# for _ in range(int(input())):
#     in_list = input().split()
#     c_name = in_list[0]
#     if len(in_list) == 2:
#         ancestor = in_list[1]
#     else:
#         ancestor = None
#     if ancestor in class_structure.keys():
#         val = class_structure[ancestor]
#         # print(val,  c_name, ancestor)
#         print("Yes" if c_name in val else "No")
#     else:
#         print("No")
#
# print(class_structure)


# https://github.com/mxmaslin/stepik/blob/master/Python%20-%20основы%20и%20применение/1.6%20Наследование%20классов%20%208.md
# classes = {}
#
#
# def add_class(classes, class_name, parents):
#     if class_name not in classes:
#         classes[class_name] = []
#     classes[class_name].extend(parents)
#     for parent in parents:
#         if parent not in classes:
#             classes[parent] = []
#
#
# def found_path(classes, start, end, path=[]):
#     path = path + [start]
#     if start == end:
#         return path
#     if start not in classes:
#         return None
#     for node in classes[start]:
#         if node not in path:
#             newpath = found_path(classes, node, end, path)
#             if newpath: return newpath
#     return None
#
#
# def answer(classes, parent, child):
#     if not (parent or child) in classes or not found_path(classes, child, parent):
#         return 'No'
#     return 'Yes'
#
#
# n = int(input())
# for _ in range(n):
#     class_description = input().split()
#     class_name = class_description[0]
#     class_parents = class_description[2:]
#     add_class(classes, class_name, class_parents)
#
# q = int(input())
# for _ in range(q):
#     question = input().split()
#     parent = question[0]
#     child = question[1]
#     print(answer(classes, parent, child))


# class ExtendedStack(list):
#     def sum(self):
#         top1 = self.pop()
#         top2 = self.pop()
#         self.append(top1 + top2)
#         return self
#
#     def sub(self):
#         top1 = self.pop()
#         top2 = self.pop()
#         self.append(top1 - top2)
#         return self
#
#     def mul(self):
#         top1 = self.pop()
#         top2 = self.pop()
#         self.append(top1 * top2)
#         return self
#
#     def div(self):
#         top1 = self.pop()
#         top2 = self.pop()
#         self.append(top1 // top2)
#         return self

# class LoggableList(Loggable, list):
#     def append(self, arg):
#         super(LoggableList, self).append(arg)
#         self.log(arg)