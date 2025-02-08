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
def st(): return sys.stdin.readline().strip()
def li(): return list(map(int, sys.stdin.readline().split()))
 
def solve():
    n = it()
    s = st()
    mpl = defaultdict(int)
    mx = 0
    mpr = Counter(s)
    l = 0
    for r in range(n):
        mpl[s[r]] += 1
        mpr[s[l]] -= 1
        if mpr[s[l]] == 0:
            del mpr[s[l]]

        mx = max(mx , len(mpl) + len(mpr))
        l += 1
    print(mx)
        
    

t = it()
for _ in range(t):
    solve()