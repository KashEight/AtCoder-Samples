import sys

sys.setrecursionlimit(10 ** 5)

n, m = map(int, input().split())

l, r = map(int, input().split())


def check(i, l, r):
    if i == m:
        return max(r - l + 1, 0)
    l_, r_ = map(int, input().split())
    nl = max(l, l_)
    nr = min(r, r_)
    i += 1
    return check(i, nl, nr)


print(check(1, l, r))