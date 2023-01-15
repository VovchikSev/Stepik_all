
"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/bPH4It1_d0c
Подвиг 4. Объявите три класса геометрических фигур: Line, Rect, Ellipse. Должна быть возможность создавать объекты каждого
класса следующими командами:

g1 = Line(a, b, c, d)
g2 = Rect(a, b, c, d)
g3 = Ellipse(a, b, c, d)
Здесь в качестве аргументов a, b, c, d передаются координаты верхнего правого и нижнего левого углов (произвольные числа).
В каждом объекте координаты должны сохраняться в локальных свойствах sp (верхний правый угол) и ep (нижний левый)
в виде кортежей (a, b) и (c, d) соответственно.
Сформируйте 217 объектов этих классов:
для каждого текущего объекта класс выбирается случайно (или Line, или Rect, или Ellipse).
Координаты также генерируются случайным образом (числовые значения). Все объекты сохраните в списке elements.
В списке elements обнулите координаты объектов только для класса Line.
P.S. На экран в программе ничего выводить не нужно.
"""
from random import randint
class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (b, c)

class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (b, c)

class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (b, c)

types = (Line, Rect, Ellipse)
elements = []
for _ in range (217):
    index = randint(0,2)
    if index == 0:
        elements.append(Line( 0, 0, 0, 0))
    else:
        elements.append(types[index](randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)))

for my_figure in elements:
    print(type(my_figure))
    # if isinstance(my_figure, Line):
    #     my_figure.sp = my_figure.ep = 0, 0
    print(my_figure.sp, my_figure.ep)

print(len(elements))