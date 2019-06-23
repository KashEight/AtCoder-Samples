n = input()
a = list(map(int, input().split()))

a.sort(reverse=True)

k = 0

for i, j in enumerate(a):
    if i % 2 == 0:
        k += j
    else:
        k -= j

print(k)