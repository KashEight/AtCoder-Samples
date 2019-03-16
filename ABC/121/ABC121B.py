n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]

t = 0

for a_i in a:
    k = 0
    for i, a_ii in enumerate(a_i):
        k += a_ii * b[i]
    if k + c > 0:
        t += 1

print(t)
