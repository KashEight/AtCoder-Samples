n, m = map(int, input().split())
ab = sorted([list(map(int, input().split())) for _ in range(n)])

t = 0

for ab_i in ab:
    if m == 0:
        break
    for i in range(ab_i[1]):
        if m == 0:
            break
        m -= 1
        t += ab_i[0]

print(t)
