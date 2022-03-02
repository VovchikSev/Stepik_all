# ОТОБРАЖЕНИЕ ТОЧЕК
import matplotlib.pyplot as plt

# КРУГ
ax = plt.gca()
circle = plt.Circle((Ox,Oy), r)
ax.add_patch(circle)

# РАДИУС
b = r*cos(pi/4)
plt.plot([Ox,Ox+b],[Oy, Oy+b],"ro")
plt.plot([Ox, Ox+b], [Oy, Oy+b], "r--", linewidth=1)

# ТОЧКИ
plt.plot(Massiv[:,0], Massiv[:,1],"bo")

# чтобы круг не был сплюснут
ax.set_aspect(1) 

# ОСИ  
plt.gca().spines["left"].set_position("center")
plt.gca().spines["bottom"].set_position("center")
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

plt.show()

# import requests
# import cProfile
 
 
# def facebook():
#     requests.get('https://facebook.com')
 
 
# def google():
#     requests.get('https://google.com')
# def twitter():
#     requests.get('https://twitter.com')
# def vk():
#     requests.get('https://vk.com')
 
 
# def main():
#     facebook()
#     google()
#     twitter()
#     vk()
# cProfile.run('main()')