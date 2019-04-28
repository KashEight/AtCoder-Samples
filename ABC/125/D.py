n = int(input())
a = list(map(int, input().split()))

k = 0
tmp = abs(a[n - 1])

for i in range(n - 1):
    if abs(a[i]) < tmp:
        tmp = abs(a[i])

    if a[i] < 0:
        a[i] *= -1
        a[i + 1] *= -1

    k += a[i]

if a[n - 1] < 0:
    if abs(a[n - 1]) == tmp:
        k += a[n - 1]
    else:
        k += abs(a[n - 1])
        k -= tmp * 2
else:
    k += a[n - 1]

print(k)
