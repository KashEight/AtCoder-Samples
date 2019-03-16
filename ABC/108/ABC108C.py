n, k = map(int, input().split())

ans = 0
t = 0

for i in range(k, n + 1, k):
    ans += 1

ans **= 3

if k % 2 == 0:
    for j in range(int(k / 2), n + 1, k):
        t += 1
    
    ans += t ** 3

print(ans)