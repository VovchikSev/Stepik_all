# ------- Экзамен  9. Итоговая работа на множества
# my_list = []
# for _ in range(int(input())):
#     my_list.append([input() for _ in range(int(input()))])
#
# # print(*my_list)
# my_set = set(my_list[0])
# for in_list in my_list:
#     my_set &= set(in_list)
# print(*sorted(my_set), sep='\n')

# my_list = [input() for _ in range(int(input()) + int(input()))]
# my_set = set()
# for fam in my_list:
#     if my_list.count(fam) == 1:
#         my_set.add(fam)
# print(len(my_set) if len(my_set) > 0 else 'NO')


# mat_count = int(input())
# inf_count = int(input())
#
# set_mat = set([input() for _ in range(mat_count)])
# set_inf = set([input() for _ in range(inf_count)])
# print(len(set_mat ^ set_inf) if len(set_mat ^ set_inf) > 0 else "NO")

# my_set = set(input().split()) | set(input().split())
# print(*sorted(my_set))


# set_quest = set([int(n) for n in input().split()])
# set_answer = set([int(n) for n in input().split()])
#
# print(("NO", "YES")[set_quest == set_answer])


# my_set = set([int(n) for n in input().split()]) & set([int(n) for n in input().split()])
# if len(my_set) > 0:
#     print(*sorted(my_set, reverse=True))
# else:
#     print('BAD DAY')


# len_1 = int(input())
# len_2 = int(input())
# myset1 = [input() for _ in range(len_1)]
# myset2 = [input() for _ in range(len_2)]
#
# for book in myset2:
#     print(("NO", "YES")[book in myset1])


# посдеднее введенное не в списке принт ОК иначе ПОВТОР
# in_count = int(input())
# my_list = [input() for _ in range(in_count + 1)]
# new_city = my_list.pop()
# print('REPEAT' if new_city in my_list else 'OK')
# через срез
# myset = {input() for _ in range(int(input()))}
# if input() in myset:
#     print('REPEAT')
# else:
#     print('OK')

# На спутнике «Восход» установлен прибор для измерения солнечной активности.
# Каждую минуту он передаёт в обсерваторию по каналу связи положительное целое число —
# количество энергии солнечного излучения. Для правильного анализа результатов нет
# необходимости держать повторяющиеся данные. Напишите программу, которая выводит максимальное количество показаний
# спутника, при удалении которых результат будет правильно проанализирован.
# На вход программе подаётся одна строка, содержащая числа – показания спутника «Восход».
# Числа указываются через пробел и не содержат ведущих нулей.
#  Sample Input 2:  1 2 3 4 5 6 7 8 9 1 2 3 Sample Output 2: 3

# my_list = [int(n) for n in input().split()]
#
# print(len(my_list) - len(set(my_list)))

# ------- Экзамен  9. Итоговая работа на множества


# set1 = frozenset('beegeek')
# set2 = frozenset('stepik')
#
# set3 = set1 & set2
# print(set3)

# files = ['python.png', 'qwerty.py', 'Python.PNg', 'apple.pnG', 'zebra.PNG',  'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git', 'ZeBrA.PnG']
#
# print(*sorted({i.lower() for i in files if '.png' in i.lower()}))


# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
# my_set = set()
# for word in sentence.split():
#     t_word = word.lower().strip('.,!():;?')
#     if 0 < len(t_word) < 4:
#         my_set.add(t_word)
# print(* sorted(my_set))
#  аналог, но какой красивый
# s = {i.strip('.,:():;!?').lower() for i in sentence.split() if len(i.strip('.,:():;!?')) < 4}
# print(*sorted(s))


# my_set = set(word.lower().strip('.,!():;?') for word in my_list)
# print(sorted(my_list))



# words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
# # my_set = set([word[0].lower() for word in words])
# print(*sorted(set([word[0].lower() for word in words])))



# items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
# print(*sorted(set(map(int, items))))


# Даны по 10-балльной шкале оценки по биологии трех учеников.
# Напишите программу, которая выводит множество оценок, не встречающихся ни у одного из трех учеников.

# student1 = set(map(int, input().split()))
# student2 = set(map(int, input().split()))
# student3 = set(map(int, input().split()))
#
# print(*sorted(set(range(11)) - (student1 | student2 | student3)))

# Даны по 10-балльной шкале оценки по физике трех учеников.
# Напишите программу, которая выводит множество оценок третьего ученика,
# которые не встречаются ни у первого, ни у второго ученика.

# student1 = set(map(int, input().split()))
# student2 = set(map(int, input().split()))
# student3 = set(map(int, input().split()))
# all_values = set([i for i in range(10)])
# print(all_values)
#
# print(*sorted(student3 - (student1 | student2), reverse=True))


# Даны по 10-балльной шкале оценки по математике трех учеников.
# Напишите программу, которая выводит множество оценок, имеющихся у учеников,
# которые встречаются не более, чем у двух из указанных учеников.
# student1 = set(map(int, input().split()))
# student2 = set(map(int, input().split()))
# student3 = set(map(int, input().split()))
#
# print(*sorted((student1 | student2 | student3) - (student1 & student2 & student3)))


# На вход программе подаются два числа. Напишите программу, определяющую, есть ли в данных числах одинаковые цифры.
# print("YES" if set(input()) >= set(input()) else "NO")


# my_list = [input() for _ in range(int(input()))]
# my_set = set(my_list[0])
# for i in my_list:
#     my_set = my_set & set(i)
#
# if len(my_set) > 0:
#     print(*sorted(my_set))
#     более красивое решение.

# my_set = set() - заполнить всеми цифрами
# for i in range(int(input())):
#     my_set &= set(input())
# print(*sorted(my_set))

# list1, list2 = [int(n) for n in input().split()], [int(n) for n in input().split()]
# my_set = set([int(n) for n in input().split()]) & set([int(n) for n in input().split()])
# print(*sorted(set([int(n) for n in input().split()]) - set([int(n) for n in input().split()])))
# my_str = input().split()
# my_set = set()
# for value in my_str:
#     if int(value) in my_set:
#         print("YES")
#     else:
#         my_set.add(int(value))
#         print("NO")

# print(my_str)




# my_list = input().lower().split()
# my_set = set()
# for my_str in my_list:
#     my_set.add(my_str.strip(".,;:-?!"))
# # print(*my_set, sep='\n')
# print(len(my_set))

# то же самое но без хранения
# for _ in range(int(input())):
#     print(len(set(input().lower())))


# myset = set()
# for i in range(10):
#     if i % 2 == 0:
#         myset.add('even')
#     else:
#         myset.add('odd')
# print(len(myset))


# my_value = input().split()
# print('YES' if set(my_value[0]) == set(my_value[1]) == set(my_value[2]) else 'NO')
# предпоследняя строка
# print(my_value[0], my_value[1], my_value[2])