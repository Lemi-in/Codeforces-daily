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

    for i in range(n):
        if arr[i] == 1:
            arr[i] += 1

    for i in range(1, n):
        if arr[i] % arr[i - 1] == 0:
            arr[i] += 1

    print(" ".join(map(str, arr)))

t = it()
for _ in range(t):
    solve()
