#author: Lemi
import sys

def cnt(temp):
    x = 1
    while temp > 1:
        temp //= 2
        x *= 2
    return x

def is_one(pos, target, num):
    if num < 2:
        return num
    if pos + 1 == 2 * target:
        return num % 2
    num //= 2
    pos //= 2
    if target > pos + 1:
        target -= (pos + 1)
    return is_one(pos, target, num)

def solve():
    n, l, r = ints()
    x = cnt(n)
    x = 2 * x - 1
    ans = sum(is_one(x, i, n) for i in range(l, r + 1))
    print(ans)

t = 1  # Single test case as per C++ code
for _ in range(t):
    solve()
