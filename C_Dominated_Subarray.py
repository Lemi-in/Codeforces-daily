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
    if n == 1 or n == len(set(arr)):
        print(-1)
    else:
        ans = float('inf')
        mp = {}
        for i in range(n):
            if arr[i] not in mp:
                mp[arr[i]] = i
            else:
                ans = min(ans,i - mp[arr[i]] + 1)
                mp[arr[i]] = i
 
        print(ans)
 
 
t = it()
for _ in range(t):
    solve()