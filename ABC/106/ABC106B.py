n = int(input())

t = 0

for i in range(1, n + 1, 2):
    k = 0
    for j in range(1, i + 1, 2):
        if i % j == 0:
            k += 1

    if k == 8:
        t += 1

print(t)