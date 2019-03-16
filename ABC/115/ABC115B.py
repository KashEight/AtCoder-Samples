n = int(input())
p = sorted(list([int(input()) for _ in range(n)]), reverse=True)

p[0] //= 2

print(sum(p))
