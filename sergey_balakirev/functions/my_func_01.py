
def foo(in_str: str):
  my_list = list(map(int, in_str.split()))
  print(f"Периметр прямоугольника, равен {(my_list[0] * 2) + ((my_list[1] * 2))}")


foo(input())
