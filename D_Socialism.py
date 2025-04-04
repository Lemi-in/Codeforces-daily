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
    n , x = ints()
    arr = li()
    arr.sort(reverse=True)
    pref = [0] * (n + 1)
    ans = 0
    for i in range(1,n + 1):
        pref[i] = pref[i - 1] + arr[i - 1]
        if pref[i] / (i) >= x:
            ans = i 
    print(ans)

 
 
t = it()
for _ in range(t):
    solve()