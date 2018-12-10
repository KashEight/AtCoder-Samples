# Failed

import copy

n, m = map(int, input().split())
s = input()
t = input()

if s[0] != t[0]:
    print(-1)
    exit(0)

if n > m:
    i = n
    j = m
    k = 0
    while True:
        if i % j == 0:
            k = j
            break
        else:
            t = copy.copy(i)
            i = copy.copy(j)
            j = t % j
    n_i = n // k
    m_i = m // k
    nm = k * n_i * m_i

    if (n - 1) * (nm / n) + 1 > nm:
        print(-1)
        exit(0)
elif m > n:
    i = m
    j = n
    k = 0
    while True:
        if i % j == 0:
            k = j
            break
        else:
            t = copy.copy(i)
            i = copy.copy(j)
            j = t % j
    n_i = n // k
    m_i = m // k
    nm = k * n_i * m_i

    if (m - 1) * (nm / m) + 1 > nm:
        print(-1)
        exit(0)

print(nm)
