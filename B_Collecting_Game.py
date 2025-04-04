# Template Author: Lemi
import sys, heapq, math
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
    

    idxA = sorted([(a[i], i) for i in range(n)])
    
    pref = [0] * n
    pref[0] = idxA[0][0]
    for i in range(1, n):
        pref[i] = pref[i - 1] + idxA[i][0]
    
    yihonal = [0] * n
    for i in range(n - 1):
        if pref[i] >= idxA[i + 1][0]:
            yihonal[i] = 1
    
    for i in range(n - 2, -1, -1):
        if yihonal[i]:
            yihonal[i] += yihonal[i + 1]
    
    result = []
    for i in range(n):  
        val, idx = idxA[i]  
        result.append((i + yihonal[i], idx))  
    
    result.sort(key=lambda x: x[1])  

    
    print(" ".join(str(x[0]) for x in result))  


t = it()
for _ in range(t):
    solve()
