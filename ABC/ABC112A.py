n = int(input())

if n == 1:
    print("Hello World")
    exit(0)

l = list(map(int, [input() for _ in range(2)]))

print(sum(l))