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
    a = li()
    rand = randint(1, 10**5)
    
    mp = defaultdict(int)
    for num in a:
        mp[num ^ rand] += 1

    uniq = set()
    for num, cnt in mp.items():
        if cnt == 1:
            uniq.add(num)

    mx = 0
    best_l, best_r = -1, -1

    l = 0
    for r in range(n):
        if a[r] ^ rand not in uniq:
            l = r + 1
        else:
            length = r - l + 1
            if length > mx:
                mx = length
                best_l, best_r = l, r

    if mx == 0:
        print(0)
    else:
        print(best_l + 1, best_r + 1)  

 
 
t = it()
for _ in range(t):
    solve()