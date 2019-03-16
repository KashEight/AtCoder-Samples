n, t = map(int, input().split())
ct = [list(map(int, input().split())) for _ in range(n)]

m = 0

for l in ct:
    if l[1] > t:
        continue
    
    if m == 0 or l[0] < m:
        m = l[0]

if m == 0:
    print("TLE")
    exit(0)

print(m)
