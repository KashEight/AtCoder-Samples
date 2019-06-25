n, l = map(int, input().split())

total = 0
dis_min = 1000000000

for i in range(n):
    taste = l + i
    total += taste
    if abs(taste) < abs(dis_min):
        dis_min = taste

print(total - dis_min)
