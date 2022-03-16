# 2.7 F-строки


# 2.6 Форматирование строк Python. Метод format
'''
Для числа 99 предыдущим будет число 98.
Для числа 99 следующим будет число 100.
'''
# my_num = int(input())
# print('Для числа {n} предыдущим будет число {f}.'.format(n=my_num, f=my_num - 1))
# print('Для числа {n} следующим будет число {f}.'.format(n=my_num, f=my_num + 1))


# 2.5 Экранированные (служебные символы) в Python
'''
вывести нечто
  /~~~\
 //^ ^\\
(/(_*_)\)
_/''*''\_
(/_)^(_\)
результат выполнения
s = "  /~~~\\\n //^ ^\\\\\n(/(_*_)\)\n_/''*''\_\n(/_)^(_\)\n"
print("  /~~~\\\n //^ ^\\\\\n(/(_*_)\)\n_/''*''\_\n(/_)^(_\)\n")
'''
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