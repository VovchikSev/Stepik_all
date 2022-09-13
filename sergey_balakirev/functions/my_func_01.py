
# def is_triangle(a:int, b:int, c:int) -> bool:
#   in_list = sorted([a, b, c])
#   print(in_list)
#   return in_list[0] + in_list[1] > in_list[2]

def is_even(in_value:int) -> bool:
  return  bool( in_value % 2)

# # while (n := int(input())) != 1:
#     # print(('', f'{n}\n')[is_even(n)], end='')
# while True:
#   value = int(input())  
#   if value == 1:
#     break
#   if is_even(value):
#     print(value)


# in_list = list(map(int, input().split()))

# print(*list(filter(is_even, in_list)))
# for value in in_list:
#   if is_even(value):
#     print(value)

def get_sq_rec(a:int, b:int)->int:
  return a * b

def get_sq_quadre(a:int)->int:
  return a * a


tp = input().strip()
if tp == "RECT":
  get_sq = get_sq_rec
else:
  get_sq = get_sq_quadre  