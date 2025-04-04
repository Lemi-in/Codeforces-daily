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
 
def solve():
    n , k  = ints()
    arr = li()
    l = 0
    t = curr = sum(arr[:k])
    for r in range(k, n):
        curr += arr[r]
        curr -= arr[l]
        l += 1
        t += curr
    print(t / (n - k + 1))

 
 
t = 1
for _ in range(t):
    solve()