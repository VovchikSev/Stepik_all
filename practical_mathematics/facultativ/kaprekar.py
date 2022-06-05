

# https://stepik.org/lesson/65382/step/1?unit=154908
def numerics(n):
    return list(map(int, str(n)))


def kaprekar_step(L):
    L.sort()
    return int("".join(map(str, L[::-1]))) - int("".join(map(str, L)))


def kaprekar_check(n):
    return len(numerics(n)) in [3, 4, 6] and len(set(numerics(n))) > 1 and n not in [100, 1000, 100000]


def kaprekar_loop(n):

    if not kaprekar_check(n):
        print(f"Ошибка! На вход подано число {n}, не удовлетворяющее условиям процесса Капрекара")
        return

    result_list = []
    while True:
        print(n)
        if n in (495, 6174, 549945, 631764):
            break
        next_n = kaprekar_step(numerics(n))
        if next_n in result_list:
            print(f"Следующее число - {next_n}, кажется процесс зациклился...")
            break
        result_list.append(next_n)
        n = next_n


kaprekar_loop(int(input()))
