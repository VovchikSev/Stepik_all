

# import turtle as t
# from random import randint
# t.speed(0)
# t.hideturtle()
# t.Screen().bgcolor("black")
# t.penup()
#
#
# def left_mouse_click(x,y):
#   t.goto(x, y)
#   t.fillcolor([randint(0,255) for _ in range(3)])
#   t.begin_fill()
#   for i in range(5):
#     t.left(144)
#     t.forward(30)
#   t.end_fill()
#
# t.Screen().onclick(left_mouse_click)
# t.Screen().listen()


# import turtle as t
# from random import randrange
#
#
# def random_color():
#     return randrange(256), randrange(256), randrange(256)
#
#
# def size():
#     return randrange(5, 45)
#
#
# def angles():
#     return randrange(5, 15)
#
#
# def left_mouse_click(x, y):
#     angle = angles()
#     n = size()
#     col = random_color()
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     t.fillcolor(col)
#     t.begin_fill()
#     for _ in range(angle):
#         t.pencolor(col)
#         t.forward(n)
#         t.right(180 - 180 / angle)
#     t.end_fill()
#
#
# t.speed(0)
# t.Screen().bgcolor('black')
# t.hideturtle()
# t.Screen().onclick(left_mouse_click)
# t.Screen().listen()

# import turtle
# import math
#
#
# turtle.Screen().setup(600, 600)
# turtle.hideturtle()
# t = 0
# turtle.color('red')
# turtle.fillcolor('red')
# turtle.begin_fill()
# while t <= 2 * math.pi:
#     x = 128 * math.sin(t) ** 3
#     y = 8 * (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t) - 5)
#     turtle.goto(x, y)
#     t += 0.01
# turtle.end_fill()
#
# turtle.done()


# import turtle as t
# from random import randrange as rnd
#
# # Параметры черепашки и экрана
# t.Screen().setup(1280, 720)
# t.Screen().colormode(255)
# t.Screen().bgcolor(10, 10, 40)
# t.tracer(25)
# t.hideturtle()
# t.speed(0)
#
#
# def draw_city(obj, col):
#     # Координаты для окон (верхний левый угол)
#     windows_coords = []
#
#     # Координаты левых верхних углов здания (для ориентирования звезд)
#     roofs = []
#
#     # Устанавливаем параметры
#     window_size = 10
#     wall_size = 5
#     ground_h = 30
#     sky_h = 20
#     windows_min_w = 5
#     windows_max_w = 10
#     windows_min_h = 1
#     windows_max_h = (720 - ground_h - sky_h - wall_size) // (wall_size + window_size)
#
#     # Координаты левого края города
#     x = -700
#     y = -360 + ground_h
#
#     obj.up()
#     obj.goto(x, y)
#
#     # Цикл рисования контура города
#     obj.down()
#     obj.color(col)
#     obj.begin_fill()
#
#     while x < 640:
#         y = - 360 + ground_h + wall_size + rnd(windows_min_h, windows_max_h + 1) * (window_size + wall_size)
#         obj.goto(x, y)
#
#         x0 = x
#         x += wall_size + rnd(windows_min_w, windows_max_w + 1) * (window_size + wall_size)
#         obj.goto(x, y)
#
#         # Добавляем координаты окон только что нарисованного здания
#         for i in range(-360 + ground_h + wall_size + window_size, y - wall_size + 1, wall_size + window_size):
#             for j in range(x0 + wall_size, x - wall_size + 1, wall_size + window_size):
#                 windows_coords.append((j, i))
#
#         # Добавляем координаты левых верхних углов здания
#         roofs.append((x0, y))
#
#     obj.goto(640, -360)
#     obj.goto(-640, -360)
#     obj.goto(-640, -360 + ground_h)
#     obj.end_fill()
#
#     # Функция возвращает два вложенныч списка с кординатами окон и крыш
#     return windows_coords, roofs
#
#
# # Функция рисования одного окна
# def draw_window(obj, coors, window_size, col):
#     obj.up()
#     obj.goto(coors)
#     obj.down()
#     obj.color(col)
#     obj.begin_fill()
#     for i in range(4):
#         obj.forward(window_size)
#         obj.right(90)
#     obj.end_fill()
#
#
# # Функция рисования одной звезды
# def draw_star(obj, coors, w, col, angle):
#     obj.up()
#     obj.goto(coors)
#     obj.down()
#     obj.right(angle)
#     obj.color(col)
#     obj.begin_fill()
#     for i in range(5):
#         obj.forward(w)
#         obj.right(144)
#     obj.end_fill()
#
#
# # Рисование силуэта города
# windows, roofs = draw_city(t, 'darkblue')
#
# # Зажигание одного окна из десяти
# for i in range(len(windows) // 10):
#     draw_window(t, windows.pop(rnd(len(windows))), 10, 'yellow')
#
# # Рисование звезд
# for i in range(200):
#     max_star_w = 5
#     while True:
#         x = rnd(-635, 636)
#         y = rnd(-360, 360)
#
#         roofs.append((636, 360))
#         for j, roof in enumerate(roofs):
#             if x > roof[0]:
#                 roof_x = roof[0]
#                 roof_y = roof[1]
#                 roof_end_x = roofs[j + 1][0]
#                 previous_roof_y = roofs[j - 1][1] if j != 0 else -360
#                 next_roof_y = roofs[j + 1][1] if j != len(roofs) - 1 else -360
#             else:
#                 break
#
#         # Условие для того, чот бы звезды не зажигались в стенах домов
#         if y > roof_y + max_star_w and (roof_x + max_star_w < x < roof_end_x - max_star_w or
#                                         (
#                                                 roof_x - 1 < x < roof_x + max_star_w + 1 and
#                                                 y > previous_roof_y + max_star_w) or
#                                         (
#                                                 roof_end_x - max_star_w - 1 < x < roof_end_x + 1) and
#                                         y > next_roof_y + max_star_w):
#             coors = x, y
#             draw_star(t, coors, rnd(max_star_w), 'yellow', rnd(360 // 5 + 1))
#             break
#
# t.done()


# import turtle as t
#
# def znak(x, i):
#   if i:
#     t.color('red')
#     t.begin_fill()
#   t.pd()
#   for _ in range(8):
#     t.fd(x)
#     t.rt(45)
#   t.up()
#
# t.ht()
# t.speed(0)
# t.width(5)
# t.up()
# for i in range(2):
#   t.goto(-50 + i * 5, 130 - i * 12)
#   znak(120 - i * 10, i)
# t.end_fill()
# t.goto(-110, -50)
# t.color('white')
# t.write('STOP', font=('Arial Narrow', 80 , 'normal'))


# import turtle as t
# t.hideturtle()
# t.Screen().setup(1000, 500)
# t.speed(0)
# t.penup()
# t.goto(-400,100)
# t.pendown()
# planets=[(100,'yellow','Солнце'),(20,'orange','Меркурий'),(30,'orange','Венера'),(23,'lightgreen','Земля'),(20,'red','Марс'),(55,'orange','Юпитер'),(50,'orange','Сатурн'),(40,'cyan','Уран'),(36,'blue','Нептун'),(10,'brown','Плутон')]
# for i in range(10):
#   x,y=t.xcor(),t.ycor()
#   t.penup()
#   t.goto(x,y-planets[i][0]-20)
#   t.fillcolor('black')
#   t.write(planets[i][2],align='center')
#   t.goto(x,y-planets[i][0])
#   t.pendown()
#   t.fillcolor(planets[i][1])
#   t.begin_fill()
#   t.circle(planets[i][0])
#   t.end_fill()
#   if i==6:
#     t2=t.Turtle()
#     t2.hideturtle()
#     t2.penup()
#     t2.goto(x-planets[i][0],y-planets[i][0]/3)
#     t2.pendown()
#     t2.right(45)
#     for loop in range(2):
#         t2.circle(planets[i][0]*1.5,90)
#         t2.circle(planets[i][0]/2,90)
#   x,y=t.xcor(),t.ycor()
#   if i!=9:
#     t.penup()
#     t.goto(x+planets[i][0]+planets[i+1][0]+20,y+planets[i][0])
#     t.pendown()


# import turtle as t
# t.ht()
# t.bk(100)
# t.fd(200)
# t.bk(100)
# t.goto(0, 100)
# t.goto(0, -100)
# t.goto(0, -30)
# t.circle(30)
# t.up()
# t.goto(-110, -5)
# t.write('Запад', align='right', font=('Arial', 12, 'normal'))
# t.goto(110, -5)
# t.write('Восток', align='left', font=('Arial', 12, 'normal'))
# t.goto(0, 110)
# t.write('Север', align='center', font=('Arial', 12, 'normal'))
# t.goto(0, -120)
# t.write('Юг', align='center', font=('Arial', 12, 'normal'))


# import turtle as t
#
# def sqw(x):
#   t.begin_fill()
#   for _ in range(4):
#     t.fd(x)
#     t.rt(90)
#   t.end_fill()
#   t.up()
#
# t.ht()
# t.speed(0)
# t.goto(-150, 150)
# sqw(300)
# t.color('white')
# for i in range(5):
#   for j in range(1 - i % 2, 5, 2):
#     t.goto(-148 + j * 60, 148 - i * 60)
#     t.pd()
#     sqw(56)


# import turtle as t
# from math import *
# import random as r
# t.Screen().setup(800, 800)
# t.ht()
# t.speed(0)
# colors = ['yellow', 'skyblue', 'orchid', 'orange', 'tomato', 'pale green']
# s = 6000
# for _ in range(5):
#   for i in range(5):
#     n = r.randint(3, 8)
#     a = sqrt(s * 4 * tan(radians(180 / n)) / n)
#     t.up()
#     t.goto(-300 + i * 130 - a / 2, 300 - _ * 120)
#     t.fillcolor(colors[r.randrange(6)])
#     t.begin_fill()
#     t.pd()
#     for j in range(n):
#       t.forward(a)
#       t.right(180 - (n - 2) / n * 180)
#     t.end_fill()


# import turtle as t
# t.Screen().bgcolor('blue')
# moon = t.Turtle()
# moon.ht()
# t.ht()
# t.dot(200, 'orange')
# t.tracer(3,0)
# for i in range(200, -200, -1):
#   moon.penup()
#   moon.goto(i,0)
#   moon.dot(201, 'blue')
#   if i < 0:
#     moon.dot(201, 'blue')
#     moon.clear()
#     moon.dot(201, 'blue')


# import turtle as t
# t.hideturtle()
# t.Screen().bgcolor('darkblue')
# t.dot(300, 'orange')
# t.fd(40)
# t.dot(300, 'darkblue')


# import turtle as t
# t.hideturtle()
# color_ = ["#FF0000", "#FFA600", "#FFFF00", "#62FF00", "#89F590", "#69C5FF", "#1E56FC", "#4800FF", "#CC00FF", "#FF5099"]
# for i in range(10):
#   t.fillcolor(color_[i])
#   t.up()
#   t.goto(0, -200 + i * 20)
#   t.begin_fill()
#   t.pd()
#   t.circle(200 - i * 20)
#   t.end_fill()


# import turtle as t
# t.hideturtle()
# t.Screen().bgcolor('white')
# t.up()
# t.goto(-150, 100)
# t.dot(80)
# t.goto(150, 100)
# t.dot(80)
# t.goto(0, -150)
# t.dot(80)
# t.goto(-150, -70)
# t.pd()
# t.width(2)
# t.goto(0, 180)
# t.goto(150, -70)
# t.goto(-150, -70)
# t.color('white')
# t.up()
# t.goto(-150, 100)
# t.fillcolor('white')
# t.begin_fill()
# t.pd()
# t.goto(150, 100)
# t.goto(0, -150)
# t.goto(-150, 100)
# t.end_fill()


# import turtle as t
# col = ['red', 'yellow', 'lime']
# t.hideturtle()
# t.begin_fill()
# t.goto(-60, 150)
# t.goto(60, 150)
# t.goto(60, -150)
# t.goto(-60, -150)
# t.goto(-60, 150)
# t.end_fill()
# t.up()
# for i in range(3):
#   t.goto(0, 90 - i * 90)
#   t.dot(80, col[i])


# import turtle as t
# t.fillcolor('#AE7759')
# t.begin_fill()
# t.goto(-100, 0)
# t.goto(0, 100)
# t.goto(100, 0)
# t.end_fill()
# t.fillcolor('#00A4E1')
# t.goto(70, 0)
# t.begin_fill()
# for _ in range(3):
#   t.rt(90)
#   t.fd(140)
# t.end_fill()


# import turtle as t
# from random import choice
#
# t.Screen().bgcolor('light blue')
# colors = ['navy', 'dark violet', 'purple', 'indigo', 'medium blue']
# sizes_snow = [4, 6, 8, 10, 12]
# sizes_pen = [1, 2, 3, 3.5]
# x_y = [(0, 0), (-140, 120), (-100, -90), (140, 60), (90, 150), (120, -130)]
# t.speed(0)
#
# for i in range(6):
#   t.penup()
#   X_Y = choice(x_y)
#   t.goto(X_Y)
#   x_y.remove(X_Y)
#   t.pendown()
#   t.pensize(choice(sizes_pen))
#   t.pencolor(choice(colors))
#   N = choice(sizes_snow)
#   for j in range(8):
#     for i in range(4):
#       t.left(45)
#       t.forward(N*0.9)
#       t.backward(N*0.9)
#       t.right(90)
#       t.forward(N*0.9)
#       t.backward(N*0.9)
#       t.left(45)
#       t.forward(N)
#     t.backward(N*4)
#     t.left(45)
#     t.dot(6)

# import turtle as t
# t.speed(10)
#
# t.circle(14)
# t.right(90)
# t.forward(82)
# t.penup()
# t.goto(0, -115)
# t.pendown()
# t.left(90)
# t.circle(82)
# t.circle(150)
# t.penup()
# t.goto(123, 140)
# t.pendown()
# t.circle(40)
# t.penup()
# t.goto(-123, 140)
# t.pendown()
# t.circle(40)
# t.penup()
# t.goto(71, 41)
# t.pendown()
# t.dot(28)
# t.penup()
# t.goto(-71, 41)
# t.pendown()
# t.dot(28)

# import turtle as t
# t.speed(8)
# t.pensize(10)
# x = [60, -60, -180, -120, -120]
# y = [80, 80, 80, 0, 0]
# colors = ['green', 'red', 'black', 'blue', 'yellow']
#
# for i in range(5):
#   t.color(colors[i])
#   t.circle(60)
#   t.penup()
#   t.goto(x[i], y[i])
#   t.pendown()

# import turtle as t
# t.hideturtle()
# t.speed(0)
# x = -150
# for _ in range(10):
#   t.color('lime')
#   t.goto(x, -180)
#   t.color('blue')
#   t.dot()
#   t.color('lime')
#   t.goto(0, 0)
#   x += 33.3
# t.color('red')
# t.dot()

# import turtle as t
# t.speed(5)
# t.color('green')
# for _ in range(3):
#   t.forward(150)
#   t.left(120)
#
# t.penup()
# t.goto(75.5, -43.3)     #150/2 = 75.5 высота малого треуг = 43,3
# t.pendown()
# t.left(60)
# t.color('yellow')
#
# for _ in range(3):
#   t.forward(150)
#   t.left(120)


# import turtle as t
#
# color_lst = ['red', 'blue', 'yellow', 'green', 'purple', 'orange']
#
# color_lst = ['red', 'blue', 'yellow', 'green', 'purple', 'orange']
# n = 0
# m = 0
# t.speed(30)
# for i in range(5, 230, 5):
#   t.pencolor(color_lst[n])
#   t.pensize(m)
#   t.forward(i)
#   t.left(45)
#   n += 1
#   m += 1
#   if n == 6:
#     n = 0

# import turtle as t
#
# t.Screen().bgcolor('pale green')
# t.pencolor('dark green')
# t.shape('turtle')
# n = 5
# for _ in range(27):
#   t.stamp()
#   t.right(30)
#   t.penup()
#   t.forward(n)
#   t.pendown()
#   n += 3

# import turtle as t
#
# t.pencolor('dark blue')
# t.Screen().bgcolor('light steel blue')
# t.shape('turtle')
# t.pensize(5)
# t.stamp()
# for _ in range(12):
#   t.penup()
#   t.forward(70)
#   t.pendown()
#   t.forward(15)
#   t.penup()
#   t.forward(15)
#   t.pendown()
#   t.stamp()
#   t.penup()
#   t.backward(100)
#   t.pendown()
#   t.left(30)

# import turtle as t
#
# t.pencolor('hot pink')
# t.Screen().bgcolor('misty rose')
# t.shape('turtle')
# t.stamp()
# for _ in range(10):
#   t.penup()
#   t.forward(50)
#   t.pendown()
#   t.stamp()
#   t.penup()
#   t.backward(50)
#   t.pendown()
#   t.left(36)


# import turtle as t
# t.pencolor('blue')
# t.Screen().bgcolor('gray')
# n = int(input())
# for _ in range(n):
#   t.dot(30)                     #размер точки можно регулировать!
#   t.forward(150)
#   t.stamp()
#   t.backward(150)
#   t.right(360/n)

# import turtle as t
# t.width(5)
# for _ in range(2):
#   t.pencolor('magenta')
#   t.dot()
#   t.pencolor('crimson')
#   t.forward(150)
#   t.pencolor('magenta')
#   t.dot()
#   t.left(90)
#   t.pencolor('crimson')
#   t.forward(60)
#   t.left(90)

# import turtle as t
# from random import choice
# colors = ['plum', 'dark green', 'royal blue', 'yellow']
# t.pensize(20)
# for _ in range(10):
#   t.pencolor(choice(colors))
#   t.dot()
#   t.penup()
#   t.forward(70)
#   t.pendown()


# import turtle as t
# t.speed(20)
# for i in range(0, 500, 10):
#   t.forward(i)
#   t.left(90)

# import turtle as t
# n = 20
# for _ in range(30):
#   t.speed = 50
#   for _ in range(4):
#     t.backward(n)
#     t.right(90)
#   n += 7

# import turtle as t
# for _ in range(5):
#   t.speed(5)
#   t.left(36)
#   t.forward(100)
#   t.left(144)
#   t.forward(100)
#   t.left(108)
#   t.forward(62)
#   t.backward(62)
#   t.left(144)

# import turtle as t
#
# def rhombus(side):
#     for _ in range(2):
#         t.forward(side)
#         t.left(120)
#         t.forward(side)
#         t.left(60)
#
# side = 100
#
# t.shape('square')  # курсор в виде квадрата
# t.color("green")  # цвет курсора
# t.width(5)  # толщина курсора
#
# rhombus(side)

# import turtle
# def hexagon(side):
#   for _ in range(6):
#     turtle.forward(side)
#     turtle.left(60)
#
# turtle.shape('arrow')     #внешний вид черепашки - стрелочка
# turtle.color('red')       #цвет курсора
# turtle.width(5)          #толщина курсора
#
# side = 50

# for _ in range(6):
#   hexagon(side)
#   turtle.left(120)
#   turtle.forward(side)
#   turtle.right(60)

# def hexagon(side):
#   import turtle
#   turtle.shape('turtle')
#   for _ in range(6):
#     turtle.forward(side)
#     turtle.left(60)
#
# hexagon(80)

# import turtle
#
# def square(side):
#     turtle.forward(side)
#     turtle.left(90)
#
#     turtle.forward(side)
#     turtle.left(90)
#
#     turtle.forward(side)
#     turtle.left(90)
#
#     turtle.forward(side)
#
#
# side = int(input('Сторона треугольника = '))
#
# square(side)
# square(side)
# square(side)
# square(side)
#
# turtle.left(45)
#
# square(side)
# square(side)
# square(side)
# square(side)

# def f(pix):
#     turtle.forward(pix)
#
# def b(pix):
#     turtle.backward(pix)
#
# def l(ang):
#     turtle.left(ang)
#
# def r(ang):
#     turtle.right(ang)
#
# def square(size, angle, count, resize):
#     for i in range(count):
#         l(angle)
#         size -= resize
#         for j in range(4):
#             f(size)
#             l(90)
#
# # square(120, 22.5, 16, 0)  # Реализация 1
# # square(120, 20, 18, 0)  # Реализация 2
# square(150, 20, 18, 6)  # Реализация 3
# turtle.done()


# def square(side):
#     for i in range(18):
#         turtle.left(20)
#         turtle.color([["#2F4F4F", "#DC143C"][i % 3 == 0], "#4B0082"][i % 3 == 2])
#         for _ in range(4):
#             turtle.forward(side)
#             turtle.left(90)
# square(100)
# turtle.done()

# turtle.shape()
# def triangle(side):
#     turtle.left(240)
#     for _ in range(3):
#         turtle.forward(side)
#         turtle.left(120)
#
#
# def proton():
#     def o():
#         turtle.left(90)
#         turtle.forward(50)
#         turtle.right(90)
#         turtle.forward(30)
#         turtle.right(90)
#         turtle.forward(50)
#         turtle.left(90)
#         turtle.forward(25)
#
#     turtle.right(60)
#     turtle.forward(150)
#     turtle.right(90)
#     turtle.forward(80)
#     for _ in range(3):
#         turtle.right(90)
#         turtle.forward(40)
#     for _ in range(2):
#         turtle.left(90)
#         turtle.forward(40)
#     turtle.forward(10)
#     turtle.left(90)
#     turtle.forward(50)
#     for _ in range(3):
#         turtle.right(90)
#         turtle.forward(25)
#     turtle.left(135)
#     turtle.forward(35)
#     turtle.left(45)
#     turtle.forward(10)
#     o()
#     turtle.left(90)
#     turtle.forward(50)
#     turtle.left(90)
#     turtle.backward(15)
#     turtle.forward(30)
#     turtle.backward(15)
#     turtle.left(90)
#     turtle.forward(50)
#     turtle.left(90)
#     turtle.forward(25)
#     o()
#     turtle.forward(15)
#     turtle.backward(30)
#     turtle.left(90)
#     turtle.forward(50)
#     turtle.right(149)
#     turtle.forward(59)
#     turtle.right(121)
#     turtle.forward(70)
#     turtle.backward(70)
#     turtle.right(90)
#     turtle.forward(50)
#     turtle.left(990)
#     turtle.forward(30)
#
# triangle(220)
# proton()

# def rectangle(width, length):
#     t.setpos(-80, 0)
#     t.shape('turtle')
#     t.color('green')
#     t.begin_fill()
#     for _ in range(2):
#         t.forward(length)
#         t.left(90)
#         t.forward(width)
#         t.left(90)
#     t.end_fill()
#     t.done()
#
# # w = int(input('Введити ширину = '))
# # h = int(input('Введити высоту = '))
# rectangle(150, 200)
# time.sleep(1)

