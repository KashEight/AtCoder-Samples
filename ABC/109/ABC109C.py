n, x = map(int, input().split())
xl = list(map(int, input().split()))

if n == 1:
    print(abs(xl[0] - x))
    exit()

xl.append(x)
xl.sort()
xl.reverse()

_d = []
d = 1

for i in range(n):
    if i == n:
        break

    _d.append(xl[i] - xl[i + 1])

for i in range(2, min(_d) + 1):
    for j in _d:
        if j % i != 0:
            break
    else:
        d = i

print(d)