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
    n, m = ints()
    mat = [li() for _ in range(n)]

    leftD = defaultdict(int)
    rightD = defaultdict(int)

    
    for i in range(n):
        for j in range(m):
            leftD[i + j] +=  mat[i][j]
            rightD[i - j] += mat[i][j]


    mx = 0
    for i in range(n):
        for j in range(m):
            mx = max(mx, leftD[i + j] + rightD[i - j] - mat[i][j])

    print(mx)
t = it()
for _ in range(t):
    solve()