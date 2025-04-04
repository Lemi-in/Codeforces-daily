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

    blueSm = arr[0]  
    redSm = 0
    blueCnt = 1
    redCnt = 0

    for k in range(1, n):  
        redSm += arr[-k] 
        redCnt += 1

        if blueCnt < n:  
            blueSm += arr[blueCnt]
            blueCnt += 1

        if redSm > blueSm: 
            print("YES")
            return

    print("NO")

t = it()
for _ in range(t):
    solve()
