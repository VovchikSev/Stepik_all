"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/HbtVara1GPI

Подвиг 8. Объявите в программе класс Cart (корзина), объекты которого создаются командой:
cart = Cart()
Каждый объект класса Cart должен иметь локальное свойство goods - список объектов для покупки
(объекты классов Table, TV, Notebook и Cup). Изначально этот список должен быть пустым.
В классе Cart объявить методы:
add(self, gd) - добавление в корзину товара, представленного объектом gd;
remove(self, indx) - удаление из корзины товара по индексу indx;
get_list(self) - получение из корзины товаров в виде списка из строк:
['<наименовние_1>: <цена_1>',
'<наименовние_2>: <цена_2>',
...
'<наименовние_N>: <цена_N>']

Объявите в программе следующие классы для описания товаров:
Table - столы;
TV - телевизоры;
Notebook - ноутбуки;
Cup - кружки.

Объекты этих классов должны создаваться командой:
gd = ИмяКласса(name, price)
Каждый объект классов товаров должен содержать локальные свойства:
name - наименование;
price - цена.

Создайте в программе объект cart класса Cart.
Добавьте в него два телевизора (TV), один стол (Table), два ноутбука (Notebook) и одну кружку (Cup).
Названия и цены придумайте сами.
P.S. Отображать на экране ничего не нужно, только создать объекты по указанным требованиям.
"""

class Cart:
    def __init__(self):
        self.goods = []
        
    def add(self, gd):
        self.goods.append(gd)
        
    def remove(self, indx):
        self.goods.pop(indx)
    
    def get_list(self):
        return [f"{x.name}: {x.price}" for x in self.goods]


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
cart = Cart()
cart.add(TV("n1TV", 200))
cart.add(TV("n2TV", 2000))
cart.add(Table("as table", 1200))
cart.add(Notebook("01", 560))
cart.add(Notebook("10", 506))
