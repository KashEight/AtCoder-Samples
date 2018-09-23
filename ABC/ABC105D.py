n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = 0

for i in range(len(a)):
    for j in range(i + 1, len(a) + 1):
        if sum(a[i:j]) % m == 0:
            ans += 1

print(ans)