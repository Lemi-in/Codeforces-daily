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
def st(): return sys.stdin.readline().strip()
def li(): return list(map(int, sys.stdin.readline().split()))
def yesNo(value): return 'YES' if value == 1 else 'NO' 
 
def solve():
    n = it()
    s = st()
    uniq = set(s)
    m = len(uniq)
    mp = defaultdict(int)
    l  = 0
    mn = len(s)
    for r in range(n):
        mp[s[r]] += 1
        while len(mp) == m:
            mn = min(mn, r - l + 1)
            mp[s[l]] -= 1
            if mp[s[l]] == 0:
                del mp[s[l]]
            l += 1
        
    print(mn)


        


 
 
t = 1
for _ in range(t):
    solve()