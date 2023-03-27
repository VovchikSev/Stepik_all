"""
Написать функцию сортировки слов в алфавитном порядке.
На вход подается строка из слов разделенных залямыми

Вывод список слов, разделенных запятыми, отсортированный по алфавиту.
При сортировке игнорировать регистр, при выводе использовать ригинальный регистр.
"""

def sort_word(list_word:str):
    result = [word.strip() for word in list_word.split(',')]
    result.sort(key=lambda x:x.lower())
    return ', '.join(result)
    # return result

if __name__ == '__main__':
    print('Naming, SHOTING, talking' == sort_word('Naming, talking, SHOTING'))