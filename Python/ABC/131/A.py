s = input()

flag = False

for i in range(1, 4):
    if s[i - 1] == s[i]:
        flag = True
        break

if flag:
    print("Bad")
else:
    print("Good")