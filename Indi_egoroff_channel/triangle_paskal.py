#  одна из реализаций труеголиника паскаля
n = int(input())
triangle = []
for index in range(n+1):
    triangle.append([1]+[0]*n)

for row_index in range(1, n+1):
    for col_index in range(1, row_index+1):
        triangle[row_index][col_index] = triangle[row_index - 1][col_index - 1] + triangle[row_index - 1][col_index]
for row in triangle:
    print(*row)

