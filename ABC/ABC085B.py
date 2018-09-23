n = int(input())
d = sorted(set(map(int, [input() for _ in range(n)])), reverse=True)

print(len(d))