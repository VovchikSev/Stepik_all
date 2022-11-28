# пример из теории.

cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
gen = (j for i in range(1000000) for j in cities)
for _ in range(20):
    print(next(gen), end=" ")


start, finish = map(int, input().split())
gen = (0.5 * pow(x / 100, 2) - 2.0 for x in range(start * 100, finish * 100 + 1))

for _ in range(20):
    print(round(next(gen), 2), end=" ")
