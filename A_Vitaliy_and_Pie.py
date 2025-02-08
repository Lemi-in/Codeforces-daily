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
def st(): return sys.stdin.readline().strip()
def li(): return list(map(int, sys.stdin.readline().split()))
 
def solve():
    n = it()
    s = st()
    cnt = defaultdict(int)
    needed = 0
    
    for i in range(len(s)):
        if i % 2 == 0:
            cnt[s[i]] += 1
        else:
            req = s[i].lower()
            if cnt[req] > 0:
                cnt[req] -= 1
            else:
                needed += 1
    
    print(needed)
 

t = 1
for _ in range(t):
    solve()