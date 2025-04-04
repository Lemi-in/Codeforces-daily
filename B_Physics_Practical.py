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
    arr.sort()
    mn = 1000000
    j = 0

    for i in range(n):
        while j < n and arr[j] <= arr[i] * 2:
            j += 1
        mn = min(mn, n - (j - i))
        j -= 1

    print(mn)

 
 
t = 1
for _ in range(t):
    solve()