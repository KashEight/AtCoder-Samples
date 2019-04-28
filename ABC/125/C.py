# Read answer

n = int(input())
a = list(map(int, input().split()))

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

left = [0 for _ in range(n + 1)]
right = [0 for _ in range(n + 1)]

for i in range(n):
    left[i + 1] = gcd(left[i], a[i])

for i in range(n - 1, -1, -1):
    right[i] = gcd(right[i + 1], a[i])

k = 0

for i in range(n):
    g = gcd(left[i], right[i + 1])

    if g > k:
        k = g

print(k)
