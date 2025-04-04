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
    arr.sort()
    sm = 0
    l , r = 0 , n - 1
    while l < r:
        sm += arr[r] - arr[l]
        l += 1
        r -= 1
    print(sm)

 
 
t = it()
for _ in range(t):
    solve()