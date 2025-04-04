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
    n , x = ints()
    arr = li()
    arr.sort()
    front = arr[:n]
    back = arr[n:]
    
    l , r = 0 , 0
    ans = 'YES'

    while l < n  and r < n :
        if back[r] - front[l] < x:
            ans = 'NO'
            break
        l += 1
        r += 1
    print(ans)

 
 
t = it()
for _ in range(t):
    solve()