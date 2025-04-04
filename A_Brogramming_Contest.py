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
    st = s()

    i = 0
    while i < n and st[i] == '0':
        i += 1  

    if i == n:
        print(0)
        return

    cnt = 1  
    for k in range(i + 1, n):
        if st[k] != st[k - 1]:
            cnt += 1

    print(cnt)

t = it()
for _ in range(t):
    solve()
