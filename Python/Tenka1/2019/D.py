n = int(input())
a = list(map(int, [input() for _ in range(n)]))
f = 998244353

def is_triangle(r, g, b):
    if r ** 2 < g ** 2 + b ** 2 and g ** 2 < r ** 2 + b ** 2 and b ** 2 < r ** 2 + g ** 2:
        return True
