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
    n , x , y = ints()
    mn = min(x, y)
    t = 0
    multi = 1
    sm = 0
    
    
    while True:
       if multi == n or sm == n:
          ans = t
          break
       sm += multi
       multi *= 2
       t += mn
    print(ans)
t = 1
for _ in range(t):
    solve()