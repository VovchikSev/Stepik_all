# 2.10 Списки и их методы

# 2.9 Списки: индексы и срезы
# top = ['Игра престолов', 'Шерлок', 'Друзья', 'Во все тяжкие', 'Доктор Хаус', 'Теория большого взрыва', 'Бригада']
# # Перед вами список топовых сериалов по версии кинопоиска. 
# # Ваша задача заменить в нем сериал "Бригада" на "Сверхъестественное" и "Друзья" на "Настоящий детектив"
# top[top.index('Бригада')] = 'Сверхъестественное'
# top[top.index('Друзья')] = 'Настоящий детектив'
# print(top)


# print(list(map(int, input().split()))[2:7])

# 2.8 Списки и операции над ними


# my_list = list(map(int, input().split()))
# print(sum(my_list) / len(my_list))


# 2.7 F-строки


# course, amount = int(input()), int(input())
# print(f"Current dollar rate is {course}. You want buy {amount} dollars")
# print(f"You must pay {amount * course}")
# # Интересный способ, через лямбду.
# # (lambda x, y: print(f'Current dollar rate is {x}. You want buy {y} dollars\nYou must pay {x * y}'))(float(input()), int(input()))


# на вход подае тся число секунд вывести в формате:
# in_secund = int(input())
# print(f"{in_secund} сек - это {in_secund // 60} мин. {in_secund % 60} сек.")
# #  интересный момент с функцией
# # (lambda x:print(f'{x} сек - это {x//60} мин. {x%60} сек.'))(int(input()))

# 2.6 Форматирование строк Python. Метод format


# '''
# Для числа 99 предыдущим будет число 98.
# Для числа 99 следующим будет число 100.
# '''
# my_num = int(input())
# print('Для числа {n} предыдущим будет число {f}.'.format(n=my_num, f=my_num - 1))
# print('Для числа {n} следующим будет число {f}.'.format(n=my_num, f=my_num + 1))


# 2.5 Экранированные (служебные символы) в Python
# '''
# вывести нечто
#   /~~~\
#  //^ ^\\
# (/(_*_)\)
# _/''*''\_
# (/_)^(_\)
# результат выполнения
# s = "  /~~~\\\n //^ ^\\\\\n(/(_*_)\)\n_/''*''\_\n(/_)^(_\)\n"
# print("  /~~~\\\n //^ ^\\\\\n(/(_*_)\)\n_/''*''\_\n(/_)^(_\)\n")
# '''
# 2.4 Комментарии в коде

# 2.3 Методы строк
# '''
# Sample Input:
# Codeforces
# Sample Output:
# .c.d.f.r.c.s
# '''
# def replace_char(symbol:str)->str:
#     if symbol in 'AOYEUI':
#         return ''
#     else:
#         return '.' + symbol.lower()

# s = "Codeforces".upper() #input().upper()
# res = ''
# for ch in s:
#     res = res + replace_char(ch)
# print(res)    

# 2.2 Строки: индексы и срезы

# 2.1 Cтроки и операции над ними