# https://stepik.org/lesson/24460/step/10?unit=6766
"""
9
add global a
create foo global
add foo b
get foo a
get foo c
create bar foo
add bar a
get bar a
get bar b

Sample Output:
global
None
bar
foo

add global a
create foo global
add foo b

get foo a

get foo c
create bar foo
add bar a
get bar a
get bar b

{
    "global": ["", set(a)]
    "foo": ["global", set(b)] смотреть есть ли в текущем словаре, 
    искомое значение. если нет ммотрим выше пока не стнет родитель = ""


}

"""
in_count = int(input())
my_dict = {"global": ["", set()]}


def get_value(ns: str, narg: str) -> str:
    result = None
    # проверить есть ли в my_dict[ns]
    if ns in my_dict.keys():
        parent, values_set = my_dict[ns]
        if narg in values_set:
            result = ns  # искомое имя в текущем пространстве.
        else:
            while parent != "":
                if parent in my_dict.keys():
                    parent_n, values_set = my_dict[parent]
                    if narg in values_set:
                        result = parent
                        break
                    else:
                        parent = parent_n
    return result


for _ in range(in_count):
    cmd, name_sp, arg = input().split()
    if cmd == "add":
        # добавить переменную в namespace
        tm_list = my_dict[name_sp]
        tm_list[1].add(arg)
        my_dict[name_sp] = tm_list

    elif cmd == "create":
        # создать namespace в arg
        my_dict[name_sp] = [arg, set()]

    elif cmd == "get":
        # получить пременную arg из namesp
        print(get_value(name_sp, arg))

print(my_dict)
"""
{'global': [None, {'a'}],
 'foo': ['global', {'b'}],
 'bar': ['foo', {'a'}]}

add global a
create foo global
add foo b
create bar foo
add bar a

a = 0
def foo():
  b = 1
  def bar():
    a = 2



"""
