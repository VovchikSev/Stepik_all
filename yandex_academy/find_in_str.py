

"""
Дана строка в UTF-8
Найти самый часто встречаюшийся символ
Если несколько символов встречаются одинаково, то вывести любой.
"""


def long_metod(st: str):
    st_set = set(st)
    ans = ''
    ans_count = 0
    for ch in st_set:
        now_count = st.count(ch)
        if now_count > ans_count:
            ans_count = now_count
            ans = ch
    print(ans, ans_count)


def first_metod(string: str):
    print(max(map(lambda x: string.count(x), string))[i])


if __name__ == '__main__':
    long_metod('ababa')
