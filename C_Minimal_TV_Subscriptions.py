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
    n , k , d = ints()
    arr = li()
    mp = defaultdict(int)
    mn = float('inf')
    l = 0 
    cnt = 0
    for r in range(n):
        mp[arr[r]] += 1
        cnt += 1
        if cnt == d:
            mn = min(mn, len(mp))
            mp[arr[l]] -= 1
            if mp[arr[l]] == 0:
                del mp[arr[l]]
            l += 1
            cnt -= 1


    print(mn)

 
 
t = it()
for _ in range(t):
    solve()