# Template Author: Lemi
import sys
import heapq
import math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
from math import ceil, sqrt, gcd

def ls(): return sys.stdin.readline().split()
def ints(): return map(int, sys.stdin.readline().split())
def strs(): return map(str, sys.stdin.readline().split())
def it(): return int(sys.stdin.readline())
def s(): return sys.stdin.readline().strip()
def li(): return list(map(int, sys.stdin.readline().split()))
 
def solve():
    n, m = ints()
    a = li()
    b = li()

    a.sort()
    b.sort(reverse=True)

    c = [b[m - n + i] for i in range(n)]

    s = sum(abs(c[i] - a[i]) for i in range(n))

    res = 0
    for k in range(n + 1):
        res = max(res, s)
        if k < n:
            s -= abs(c[k] - a[k])
            c[k] = b[k]
            s += abs(c[k] - a[k])

    print(res)



t = it()
for _ in range(t):
    solve()