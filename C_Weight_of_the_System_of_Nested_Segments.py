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
    space = input()
    n , m = ints()
    points = []
    
    for i in range(1, m + 1):
        x, w = ints()
        points.append((x, w, i))
    
    points.sort(key=lambda p: p[1])
    selected = points[:2 * n]
    
    total_weight = sum(p[1] for p in selected)
    
    selected.sort(key=lambda p: p[0])
    
    pairs = []
    for i in range(n):
        pairs.append((selected[i][2], selected[2 * n - 1 - i][2]))
    
    print(total_weight)
    for a, b in pairs:
        print(a, b)

t = it()
for _ in range(t):
    solve()
    print()