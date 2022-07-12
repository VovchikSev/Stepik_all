

# if __name__ == "__main__":

# in_value = int(input())
# while in_value < 100:
#     print(*list(filter(lambda val: not (val % 3) and not val % 5, [value for value in range(1, in_value + 1)])))
#     break
# else:
#     print("слишком большое значение n")

# in_value = int(input())
# start = 1
# in_day = 10
# while in_day < in_value:
#     in_day *= 1.1
#     start += 1
# print(start)

lst_in = ["Муму", "Евгений Онегин", "Сияние", "Мастер и Маргарита", "Пиковая дама", "Колобок"]
# lst_out = []
while lst_in:
    value = lst_in.pop(0)
    if len(value.split()) == 1:
        print(value, end=" ")
        # lst_out.append(value)
# print(*lst_out)

