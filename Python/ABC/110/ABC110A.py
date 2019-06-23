i = sorted(list(map(int, input().split())), reverse=True)

print(int("{}{}".format(str(i[0]), str(i[1]))) + i[2])
