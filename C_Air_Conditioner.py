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
    n, m = ints()
    
    t = [0] * 160
    L = [0] * 160
    R = [0] * 160

    for i in range(1, n + 1):
        t[i], L[i], R[i] = ints()

    l = m
    r = m
    for i in range(1, n + 1):
        time_passed = t[i] - t[i - 1]
        l -= time_passed
        r += time_passed

        if R[i] < l or L[i] > r:
            print("NO")
            break
        l = max(l, L[i])
        r = min(r, R[i])
    else:
        print("YES")

 
 
t = it()
for _ in range(t):
    solve()