n = int(input())
xyh = [list(map(int, input().split())) for _ in range(n)]

for i in range(0, 101):
    for j in range(0, 101):
        tl = []
        for l in xyh:
            h = abs(l[0] - i) + abs(l[1] - j) + l[2]
        
        ts = set(tl)
        if len(ts) == 1:
            print("{} {} {}".format(i, j, tl[0]))
            exit(0)
