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
    n, k = ints()
    a = li()
    b = li()
    rand = randint(1, 10**5)  
    a.sort()
    b.sort()
    n = len(a)
    m = len(b)
    mp = defaultdict(int)
    for l in a:
        mp[l ^ rand] += 1
    for l in b:
        mp[l ^ rand] += 1
    both = [key ^ rand for key in mp.keys()]
    
    
    mx = 0
    for price in both:
        t = n - bisect_right(b, price - 1) 
        h = n - bisect_left(a, price)   
        neg = t - h  
        
        if neg <= k:
            mx = max(mx, t * price)
    print(mx)

t = it()
for _ in range(t):
    solve()