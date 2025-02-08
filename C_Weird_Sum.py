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
def compute(points):
    xs = sorted(p[0] for p in points)
    ys = sorted(p[1] for p in points)

    def computeEach(arr):
        n = len(arr)
        t = 0
        prefix = 0
        
        for i in range(n):
            t += arr[i] * i - prefix
            prefix += arr[i]
        
        return t

    smX = computeEach(xs)
    smY = computeEach(ys)

    return smX + smY


 
def solve():
    n , m = ints()
    mat = [li() for _ in range(n)]
    mp = defaultdict(list)
    for i in range(n):
        for j in range(m):
            mp[mat[i][j]].append([i,j])
    vals = [val for key, val in mp.items()]
    
    total = 0
    for val in vals:
        total += compute(val)
    print(total)
   


t = 1
for _ in range(t):
    solve()