# Template Author: Lemi
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

def even(n):
    return n % 2 == 0
 
def solve():
    n = it()
    arr = li()
    original = [a for a in arr]
    odds = sorted([o for o in arr if o % 2 != 0])
    evens = sorted([e for e in arr if e % 2 == 0])
    o = 0
    e = 0
    for i in range(n):
        if even(arr[i]):
            if e < len(evens):
                arr[i] = evens[e]
                e += 1
        else:
            if o < len(odds):
                arr[i] = odds[o]
                o += 1
    if arr == sorted(original):
        print('YES')
    else:
        print('NO')
    
 
t = it()
for _ in range(t):
    solve()