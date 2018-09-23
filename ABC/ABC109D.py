h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

i = 0

for j, b in enumerate(a):
    if sum(b) % 2 == 0:
        for k, c in enumerate(b):
            if c % 2 == 1:
                if j == 0:
                    pass
