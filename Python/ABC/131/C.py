from fractions import gcd

a, b, c, d = map(int, input().split())

nums = b - a + 1
c_count = b // c - a // c + 1 if a % c == 0 else b // c - a // c
d_count = b // d - a // d + 1 if a % d == 0 else b // d - a // d
lcm = c * d // gcd(c, d)
lcm_count = b // lcm - a // lcm + 1 if a % lcm == 0 else b // lcm - a // lcm
print(nums - c_count - d_count + lcm_count)
