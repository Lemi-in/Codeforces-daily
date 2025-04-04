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
    n = it()
    arr = li()
    m = it()
    qu = li()
    arr.sort(reverse=True)
    sm = sum(arr)
    for q in qu:
        print(sm - arr[q - 1])

 
t = 1
for _ in range(t):
    solve()