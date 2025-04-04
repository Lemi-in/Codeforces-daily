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
    n, m = ints()
    arr = li()
    mp = {}
    ans = 0
    for x in arr:
        if x not in mp:
            mp[x] = 0
        mp[x] += 1
    for x in mp:
        y = mp[x]
        l = min(m // x, y)
        ans = max(ans, l * x)
        if x + 1 not in mp:
            continue
        y = mp[x + 1]
        for i in range(1, l + 1):
            r = min((m - i * x) // (x + 1), y)
            val = i * x + r * (x + 1)
            ans = max(ans, val)
    print(ans)
 
 
t = it()
for _ in range(t):
    solve()