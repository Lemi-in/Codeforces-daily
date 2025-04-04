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
    A = li()
    m = it()
    B = li()

    if sum(A) != sum(B):  
        print(-1)
        return

  
    i, j = 0, 0
    sumA, sumB = 0, 0
    count = 0

    while i < n or j < m:
        if sumA == sumB and sumA > 0: 
            count += 1
            sumA = sumB = 0

        if sumA < sumB or i < n and j == m: 
            sumA += A[i]
            i += 1
        else: 
            sumB += B[j]
            j += 1

    print(count + 1) 

t = 1
for _ in range(t):
    solve()
