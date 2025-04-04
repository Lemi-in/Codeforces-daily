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
def st(): return sys.stdin.readline().strip()
def li(): return list(map(int, sys.stdin.readline().split()))
def yesNo(value): return 'YES' if value == 1 else 'NO' 
def find(arr):
    mx = float('-inf')
    curr = 0
    start = 0
    mxStart = 0
    mxEnd = 0
    n = len(arr)
 
    for i in range(n):
        if curr == 0:
            start = i  
        
        curr += arr[i]
 
        if curr > mx:
            mx = curr
            mxStart = start
            mxEnd = i
        
        if curr < 0:
            curr = 0  
    if mxStart == 0 and mxEnd == n - 1:
        return -1
 
    return mx
def solve():
    n = it()
    arr = li()
    total = sum(arr)
    mx = find(arr)

    print(yesNo(total > mx))
 
 
t = it()
for _ in range(t):
    solve()