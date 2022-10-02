
# замыкания
# Подвиг 1. Используя замыкания функций, определите вложенную функцию, которая бы увеличивала значение 
# переданного параметра на 5 и возвращала бы вычисленный результат. При этом внешняя функция должна иметь 
# следующую сигнатуру: def counter_add(): ...


def counter_add(in_param:int):
    def inner_counter():
        nonlocal in_param
        in_param += 5
        return in_param
    return inner_counter

k = int(input())
cnt = counter_add
print(cnt(k))