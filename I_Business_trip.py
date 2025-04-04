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
    k = it()
    arr = li()
    arr.sort(reverse=True)
    cnt = 0
    sm = 0
    for a in arr:
        if sm >= k:
            break
        sm += a
        cnt += 1
    if sm < k:
        print(-1)
    else:
        print(cnt)
 
 
t = 1
for _ in range(t):
    solve()