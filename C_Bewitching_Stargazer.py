#author: Lemi
import sys

def solve():
    n, k = ints()
    mul, total, cur = n + 1, 0, 1

    while n >= k:
        if n & 1:
            total += cur
        n >>= 1
        cur <<= 1

    print((mul * total) // 2)

t = it()
for _ in range(t):
    solve()
