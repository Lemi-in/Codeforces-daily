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
    n , k = ints()
    arr = li()
    mx = 0
    mp = defaultdict(int)
    l  = 0 
    x , y = -1 , - 1
    for r in range(n):
        mp[arr[r]] += 1
        while l < n and len(mp) > k:
            mp[arr[l]] -= 1
            if mp[arr[l]] == 0:
                del mp[arr[l]]
            l += 1
        if  r - l + 1 >= mx:
            x  , y = l + 1 , r + 1
            mx = max(mx, r - l + 1)
    print(x , y)

 
 
t = 1
for _ in range(t):
    solve()