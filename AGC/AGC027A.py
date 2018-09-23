n, x = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse=True)

i = 0

for j in a:
    x -= j
    if x < 0:
        break
    
    i += 1

print(i)