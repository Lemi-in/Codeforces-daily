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
    n, m = ints()
    song = [ints() for _ in range(n)]
    arr = li()
    time = [x * y for x, y in song]
 
    for d in range(1, len(time)):
        time[d] += time[d - 1]
    
    i, d, res = 0, 0, []
 
    while i < len(arr) or d < len(time):
        if d == len(time) or i < len(arr) and arr[i] <= time[d]:
            res.append(d + 1)
            i += 1
        else:
            d += 1
        
    for r in res:
        print(r)
 
 
 
 
 
 
 
solve()