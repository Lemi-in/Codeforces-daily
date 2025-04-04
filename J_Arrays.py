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
    na , nb = ints()
    k , m = ints()
    a = li()
    b = li()
    b.sort(reverse=True)
    less = [a[i] for i in range(k)]
    more = [b[i] for i in range(m)]
    ans = 'YES'
    more.sort()

    if less[-1] >= more[0]:
        ans = 'NO'
    print(ans)

 
 
t = 1
for _ in range(t):
    solve()