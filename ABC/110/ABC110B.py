n, m, x, y = map(int, input().split())
xi = sorted(list(map(int, input().split())), reverse=True)
yi = sorted(list(map(int, input().split())), reverse=True)

xi.append(x)
yi.append(y)

if max(xi) >= min(yi):
    print("War")
    exit(0)

print("No War")