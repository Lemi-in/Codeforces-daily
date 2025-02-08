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
def s(): return sys.stdin.readline().strip()
def li(): return list(map(int, sys.stdin.readline().split()))
 
def solve():
    x , y = ints()
    arr.append((x, y))
 
s , n = ints()
arr = []
for _ in range(n):
    solve()

arr.sort(key=lambda x:(x[0], -x[1]))
ans = 'YES'
for x , y in arr:
    if s <= x:
        ans = 'NO'
        break
    s += y

print(ans)