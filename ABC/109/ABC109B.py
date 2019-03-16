n = int(input())
w = [input() for _ in range(n)]

s = set()
l = []

for c in w:
    s.add(c)
    l.append([c[0], c[len(c) - 1]])

if len(s) != len(w):
    print("No")
    exit()

for i in range(len(l)):
    if i == len(l) - 1:
        break
    
    if l[i][1] != l[i + 1][0]:
        print("No")
        exit()

print("Yes")