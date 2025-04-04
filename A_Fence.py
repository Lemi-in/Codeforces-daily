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
    n, k = ints()
    h = li()
    s = sum(h[:k])
    m, j = s, 0
    for i in range(1, n - k + 1):
        s += h[i + k - 1] - h[i - 1]
        if s < m:
            m, j = s, i
    print(j + 1)

    
 
t = 1
for _ in range(t):
    solve()