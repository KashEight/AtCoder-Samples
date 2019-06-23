# Read answer

n = int(input())
s = input()

w = s.count(".")
b = 0
k = w

for c in s:
    if c == ".":
        w -= 1
    else:
        b += 1
    k = min(k, w + b)

print(k)
