n, k = map(int, input().split())
h = sorted(list([int(input()) for _ in range(n)]), reverse=True)

t = 0

for i in range(n - k + 1):
    _t = h[i] - h[i + k - 1]
    if _t == 0:
        print(0)
        exit()
    else:
        if t == 0 or _t < t:
            t = _t

print(t)
