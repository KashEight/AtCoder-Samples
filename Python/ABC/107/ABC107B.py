h, w = map(int, input().split())
a = [[s for s in input()] for _ in range(h)]

b = []

for i in range(h):
    for j in range(w):
        if a[i][j] == "#":
            b.append([i, j])

