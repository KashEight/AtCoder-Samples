n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))

vc = sorted([v[i] - c[i] for i in range(n)], reverse=True)

k = 0

for vc_i in vc:
    if vc_i > 0:
        k += vc_i

print(k)
