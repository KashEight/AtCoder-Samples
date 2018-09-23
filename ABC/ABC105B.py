n = int(input())

for i in range(n // 7 + 1):
    for j in range((n - 7 * i) // 4 + 1):
        if 7 * i + 4 * j == n:
            print("Yes")
            exit()

print("No")