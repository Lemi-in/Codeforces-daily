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
    a = li()
    
    seen = [False] * (n + 1)  
    b = [0] * n  
    
    for i in range(n):
        if not seen[a[i]]:
            b[i] = a[i]
            seen[a[i]] = True

    missing = deque(i for i in range(1, n + 1) if not seen[i])

    for i in range(n):
        if b[i] == 0:
            b[i] = missing.popleft()

    print(" ".join(map(str, b)))

   

t = it()
for _ in range(t):
    solve()