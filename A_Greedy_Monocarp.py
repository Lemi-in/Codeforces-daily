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
    n , k = ints()
    arr = li()
    sm = 0
    arr.sort(reverse=True)
    i = 0
    while i < n:
        sm += arr[i]
        if sm > k:
            sm -= arr[i]
            break
        elif sm == k:
            break
        i += 1
    if sm < k:
        ans = k - sm
    else:
        ans = 0
    print(ans)
        
 
 
t = it()
for _ in range(t):
    solve()