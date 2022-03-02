pokemons = ['Aerodactyl', 'Pikachu', 'Regigigas', 'Quilava']
name = 'Pikachu'
index = pokemons.index(name)
print(index)

# сделать елочку из нечетного количества снежинок * или же произвольной высоты



# # сделать игру с угадыванием числа, игра оканчивается с угадыванием числа, указывать перебор недобор
# import random
# min_value = random.randint(1, 50)
# max_value = random.randint(min_value, 150)
# secret_value = random.randint(min_value, max_value)
# print(min_value, max_value)
# # centr = max_value - min_value
# user_value = 0
# while True:
#     #  доработать подсказку по поиску центрального числа
#     centr = max_value - min_value
#     user_value = int(input(f'Центр = {centr}: '))
#     if user_value == secret_value or user_value < 1:
#         break
#     elif user_value < secret_value:
#         min_value = user_value
#         print('недобор!')
#     elif user_value > secret_value:
#         max_value = user_value
#         print('перебор!')
    
# print(secret_value)
# heights = [5642, 8611, 5193, 4810]
# names = "Эльбрус", "К2", "Шхара", "Монблан"  

# # highest_value = max(heights)
# # highest_name = names[heights.index(highest_value)]
# highest_value, highest_name = max(zip(heights, names))
# print(max(zip(heights, names)))

# print(highest_name, highest_value)  #  max(my.keys))

# qualities = ['Любознательный', 'Яростный', 'Меланхоличный']
# entities = ['Василиск', 'Единорог', 'Дракон']
# for index in range(len(qualities)):
#     print(f"{qualities[index]} {entities[index]}")
# # [print(qualities[i], entities[i]) for i in range(len(qualities))]    

# print('Го!' if all([ not is_busy, want_to_go, is_nice_weather]) else 'Не выходи из комнаты, не совершай ошибку')

# for value in range(11):
#     print(f'9 x {value} = {9 * value}')
# # [print(f'{9} x {i} = {9*i}') for i in range(11)]

# n = 7
# operation = "sum" # "product"
# result = 1
# for value in range(2, n + 1):
#     if operation == "sum":
#         result += value
#     else:
#         result *= value   
# print(result)             


# males = ['Джонатан', 'Дио', 'Спайк']
# females = ['Фэй', 'Эрина', 'Лина']
# for index in range(len(males)):
#     males[index] += "-кун"
#     females[index] += "-тян"
# print(males)    
# print(females)

# leap_years = [year for year in range(2025, 3025 ) if (not year % 4  and year % 100)  or not (year % 400)][:20]
# print(leap_years)


# max_len = 7
# for value in range(1, max_len + 1):
#     print("*" * value)
# # print(*['*' * _ for _ in range(1, max_len + 1)], sep = '\n')


# length, width = 9, 2 
# for _ in range(length):
#     print('*' * width)
# print(('*' * width + '\n') * length)



# ingredients = ['flower', 'sugar', 'egg', 'honey', 'apple', 'cherry', 'milk']
# chosen_ingredients = [ingredients[index] for index in range(len(ingredients)) if not index % 3]        
# print(chosen_ingredients)    


# f, t = 5, 58 # 807
# summ = sum( filter(lambda val: any([not val %3 , not val % 5]),  [value for value in range(f, t + 1)]))
# print(summ)


# words = ['Hi', 'there', 'I am', 'list', 'with', 'words']
# length = 0
# for _ in words:
#     length += 1

# print(len(words), length)
# from functools import reduce
# length = reduce(lambda i, _: i + 1, words, 0)


# sums = [1, 1, 0, 10, 2, 10, 15]
# total = 0
# for value in sums: 
#     total += value

# # А-а, с функцией sum кто угодно решит, а ты попробуй без неё
# from functools import reduce
# from operator import add
# total = reduce(add, sums)    
