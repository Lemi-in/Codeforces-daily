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
    n = it()
    arr = li()
    
    mp = Counter(arr)  
    uniQ = set(mp.values())
    mn = n  
   
    for u in uniQ:
        remove = 0
        for f in mp.values():
            if f < u:
                remove += f
            else:
                remove += f - u
        mn = min(mn, remove)
        

    print(mn)

t = it()
for _ in range(t):
    solve()

print(83 * 83)
