s, t = [input() for _ in range(2)]

while True:
    if s == "":
        break

    s = s.replace(s[0], "")
    t = t.replace(t[0], "")
    
    if len(s) != len(t):
        print("No")
        exit(0)

print("Yes")
