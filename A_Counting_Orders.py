# Template Author: Lemi
import sys, heapq,math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
from math import ceil, sqrt, gcd

def ls(): return sys.stdin.readline().split()
def ints(): return map(int, sys.stdin.readline().split())
def strs(): return map(str, sys.stdin.readline().split())
def it(): return int(sys.stdin.readline())
def s(): return sys.stdin.readline().strip()
def li(): return list(map(int, sys.stdin.readline().split()))
def yesNo(value): return 'YES' if value == 1 else 'NO' 

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
 
 
def solve():
    n = it()
    a = li()
    b = li()
    a.sort()
    b.sort()
    ans = -1
    for i in range(n):
        if a[i] <= b[i]:
            ans =  0
    if ans == 0:
        print(0)
        return
    l , r = 0 , 0
    res = 1
    while l < n:
        while r < n and a[l] > b[r]:
            r += 1

        res *= (r - l) 
        res %= p
        l += 1

    print(res % p)

t = it()
for _ in range(t):
    global p
    p = (pow(10,9) + 7)
    solve()