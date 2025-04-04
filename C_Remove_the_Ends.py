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

    n = it()
    
    a = li()
    
    pref = [0] * (n + 1)
    sufx = [0] * (n + 1)
    
    for i in range(n):
        pref[i + 1] = pref[i] + max(0, a[i])
    
    for i in range(n - 1, -1, -1):
        sufx[i] = sufx[i + 1] + max(0, -a[i])
    
    mx = 0
    for i in range(n + 1):
        if pref[i] + sufx[i] > mx:
            mx = pref[i] + sufx[i]
    
    print(mx)


 
 
t = it()
for _ in range(t):
    solve()