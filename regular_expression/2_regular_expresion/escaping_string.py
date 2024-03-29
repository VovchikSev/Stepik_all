# https://stepik.org/lesson/701290/step/1?unit=701347
# Экранирование и строки в Python
'''
Как вы уже наверное знаете, в строках Python по умолчанию работает экранирование:

# Вместо \n мы получим переход на новую строку
print("Переносим\nстроку")

# Вместо \\' получаем вывод \'
# Первый \ экранирует второй \, и он исчезает из вывода 
print("\\'")
Вместо такого вывода:
Переносим\nстроку
\'
получаем такой:
Переносим 
строку
\'

Всё это из-за того, что в Python существуют специальные (их ещё называют экранируемые или управляющие) 
последовательности, которые заменяются на другие символы. 
Например, последовательность символов \n в примере выше стала символом перехода на новую строку.

Чтобы сказать интерпретатору, что экранировать последовательность не нужно, достаточно поставить перед ней 
обратный слеш:

    # Теперь тут выводится строка: Переносим\nстроку
    print("Переносим\\nстроку")

    # Вместо вывода, который мы ожидали, снова получаем такой: \'
    print("\\\'")

    # Для того, чтобы исправить эту ситуацию, добавим ещё один обратный слеш!
    print("\\\\'")
    # И только сейчас мы получим вывод: \\'
Иногда, как в примере выше, одного слеша бывает недостаточно, и приходится добавлять больше. 
Как вы уже поняли, использовать такой способ бывает не очень удобно.

Экранирование в регулярных выражениях
В регулярных выражениях тоже есть экранирование. Каждое регулярное выражение, которое используется в коде, 
компилируется интерпретатором, и заменяет управляющие последовательности на другие символы. Если нам нужно использовать 
какой-то спецсимвол как простой текст, то достаточно поставить перед ним \, как и в обычных строках Python. 
Это работает со всеми спецсимволами!

Пример: 
В регулярных выражениях есть спецсимвол ., который по умолчанию заменяет любой символ, 
кроме символа перехода на новую строку. Чтобы его экранировать и использовать как обычный символ точки, 
мы запишем его вот так: \..

2 экранирования сразу?
Да, это возможно. Если вы используете обычную строку в регулярном выражении, 
то сначала срабатывает экранирование строки в Python, а потом срабатывает второе экранирование при компиляции 
регулярного выражения.

Мы уже заметили, что с обычным экранированием в строках Python справиться довольно сложно, а двойное экранирование 
только добавляет проблем.

На помощь приходят сырые строки!
Не отчаивайтесь! Именно в этом случае нас спасут сырые строки. С помощью них мы отключим экранирование в строках Python 
и будем работать только с одним экранированием - экранированием в регулярных выражениях.
Согласитесь, что намного удобнее отключить экранирование с помощью сырых строк, вместо того, чтобы отключать экранирование
у каждой последовательности отдельно с помощью обратных слешей:
    # Отключаем экранирование всей строки префиксом r:
    print(r"Переносим\nстроку")
    print(r"\\'")

    # Отключаем экранирование каждой последовательности с помощью слешей:
    print("Переносим\\nстроку")
    print("\\\\'")
'''
def out_values(a:int, b:int):
    print(rf"{a}\n + \n{b}\n = \n{a+b}")

if __name__ == '__main__':
    first, second = int(input()), int(input())
    out_values(first, second)
