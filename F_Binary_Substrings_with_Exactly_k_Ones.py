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

def count(s, k):
    ans = 0
    l = 0
    n = len(s)
    cnt = 0

    for r in range(n):
        if s[r] == '1':
            cnt += 1
        while l <= r and cnt > k:
            if s[l] == '1':
                cnt -= 1
            l += 1
        ans += (r - l + 1)

    return ans

def solve():
    k = it()
    s = st()
    ans = count(s, k) - count(s, k - 1)
    print(ans)
 
 
t = 1
for _ in range(t):
    solve()