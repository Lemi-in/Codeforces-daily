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
    n, m = ints()
    k = li()
    c = li()
 
    k.sort()
    used = [0] * n
 
    cnt = n - 1
 
    i = 0
    while i < m or cnt != -1:
        used[cnt] = min(c[i], c[k[cnt] - 1])
        if i < m - 1:
            i += 1
        if cnt > 0:
            cnt -= 1
        else:
            break
 
    print(sum(used))
 
 
 
t = it()
for _ in range(t):
    solve()