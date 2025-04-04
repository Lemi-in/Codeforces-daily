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
    arr = li()
    
    t = sum(arr)
    
    mx = float('-inf')
    curr = 0
    for i in range(n-1):  
        curr += arr[i]
        mx = max(mx, curr)
        if curr < 0:
            curr = 0
    
    sufx = float('-inf')
    curr = 0
    for i in range(n-1, 0, -1):  
        curr += arr[i]
        sufx = max(sufx, curr)
        if curr < 0:
            curr = 0
    
    
    if t > max(mx, sufx):
        print("YES")
    else:
        print("NO")
    
t = it()
for _ in range(t):
    solve()
