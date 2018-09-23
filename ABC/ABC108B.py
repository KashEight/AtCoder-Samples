x1, y1, x2, y2 = map(int, input().split())

vector_x, vector_y = x2 - x1, y2 - y1
print(x2 - vector_y, y2 + vector_x, x1 - vector_y, y1 + vector_x)
