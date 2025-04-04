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

import sys

def solve():
    n, m, k = ints()
    a = sorted(s()) 
    b = sorted(s())  

    i, j = 0, 0  
    cntA, cntB = 0, 0  
    c = ""

    while i < n and j < m:
        if (cntA < k and (cntB == k or a[i] < b[j])):  
            c += a[i]
            i += 1
            cntA += 1
            cntB = 0 
        else: 
            c += b[j]
            j += 1
            cntB += 1
            cntA = 0  
    print(c)

t = it()
for _ in range(t):
    solve()
