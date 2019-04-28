a, b, c = map(int, input().split())

if a > b:
    if b <= c <= a:
        print("Yes")
        exit()
else:
    if a <= c <= b:
        print("Yes")
        exit()

print("No")
