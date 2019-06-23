# Failed
n = int(input())
v = list(map(int, input().split()))

_v = set(v)

if len(_v) == 1:
    print(int(n / 2))
    exit(0)

_v1 = set(v[0::2])
_v2 = set(v[1::2])

c1, c2 = 0, 0
i1, i2 = 0, 0

for i in _v1:
    if v.count(i) > c1:
        c1 = v.count(i)
        i1 = i

for i in _v2:
    if v.count(i) > c2:
        c2 = v.count(i)
        i2 = i

v.remove(i1)
v.remove(i2)

t = set(v)

print(len(v))
