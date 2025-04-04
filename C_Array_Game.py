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
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = []
    ans0 = min(a)
    if k == 1:
        for i in range(n - 1):
            ans0 = min(ans0, a[i + 1] - a[i])
    elif k == 2:
        for i in range(n - 1):
            ans0 = min(ans0, a[i + 1] - a[i])
        for i in range(n):
            for j in range(i + 1, n):
                x = a[j] - a[i]
                k = bisect_left(a, x)
                if k - 1 >= 0:
                    ans0 = min(ans0, x - a[k - 1])
                if k < n:
                    ans0 = min(ans0, a[k] - x)
    else:
        ans0 = 0
    ans.append(ans0)
    for a in ans:
        print(a)
 
 
t = it()
for _ in range(t):
    solve()