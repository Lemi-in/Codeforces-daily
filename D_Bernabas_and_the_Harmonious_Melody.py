# Template Author: Lemi
import sys, heapq, math
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

def mnDelete(s):
    def minRemove(ch):
        l, r = 0, len(s) - 1
        d = 0

        while l < r:
            if s[l] == s[r]: 
                l += 1
                r -= 1
            elif s[l] == ch:  
                l += 1
                d += 1
            elif s[r] == ch: 
                r -= 1
                d += 1
            else:  
                return float('inf')

        return d

 
    if s == s[::-1]:
        return 0

  
    mn = float('inf')
    for ch in set(s):  
        mn = min(mn, minRemove(ch))

    return mn if mn != float('inf') else -1

def solve():
    n = it()  
    s = st()
    print(mnDelete(s))

t = it()
for _ in range(t):
    solve()
