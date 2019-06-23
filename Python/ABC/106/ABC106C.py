s = list(input())
k = int(input())

for i, j in enumerate(s):
    if i + 1 >= k:
        print(j)
        exit()

    if j == "1":
        continue
        
    print(j)
    exit()
