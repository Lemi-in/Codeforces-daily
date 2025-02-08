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
    for i in range(n - 1):
        mn = min(arr[i], arr[i + 1])
        arr[i] -= mn
        arr[i + 1] -= mn
    ans = 'YES'
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            ans = 'NO'
            break
    print(ans)
 
 
t = it()
for _ in range(t):
    solve()