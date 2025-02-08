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

def check(s):
    return s == s[::-1]

def solve():
    s = st()
    mp = Counter(s)
    if len(mp) == 1:
        if 'a' in mp:
            print('NO')
        else:
            print('YES')
            print(s + 'a')
    else:
        print('YES')
        a = 'a'+ s
        b = s + 'a'
        if not check(a):
            print(a)
        else:
            print(b)
    
t = it()
for _ in range(t):
    solve()