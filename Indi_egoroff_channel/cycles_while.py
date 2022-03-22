
"""doc."""
# 4  Цикл while
# 4.1 Знакомство с циклом while

x, y = map(int, input().split())
day = 1
while x < y:
    x *= 1.15
    day += 1
print(day)    