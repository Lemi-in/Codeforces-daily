# Template Author: Lemi
import sys, heapq,math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
from math import ceil, sqrt, gcd
from random import randint

def ls(): return sys.stdin.readline().split()
def ints(): return map(int, sys.stdin.readline().split())
def strs(): return map(str, sys.stdin.readline().split())
def it(): return int(sys.stdin.readline())
def s(): return sys.stdin.readline().strip()
def li(): return list(map(int, sys.stdin.readline().split()))
def yesNo(value): return 'YES' if value == 1 else 'NO' 
 
def solve():
    n, m, k = ints()
    a = li()
    op = [tuple(ints()) for _ in range(m)]
    q = [tuple(ints()) for _ in range(k)]

    cnt = [0] * (m + 2)
    for x, y in q:
        cnt[x] += 1
        cnt[y + 1] -= 1

    for i in range(1, m + 1):
        cnt[i] += cnt[i - 1]

    diff = [0] * (n + 2)
    for i in range(m):
        l, r, d = op[i]
        diff[l] += d * cnt[i + 1]
        diff[r + 1] -= d * cnt[i + 1]

    for i in range(1, n + 1):
        diff[i] += diff[i - 1]
        a[i - 1] += diff[i]

    print(*a)

    
 
t = 1
for _ in range(t):
    solve()