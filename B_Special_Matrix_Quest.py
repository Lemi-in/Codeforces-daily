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

def columns(matrix):
    if not matrix:
        return []
    
    num_cols = len(matrix[0])
    return [[row[i] for row in matrix] for i in range(num_cols)]
def diagonal(mat):

    n , m = len(mat), len(mat)
    mp = defaultdict(list)
    for i in range(n):
        for j in range(m):
            mp[(i + j)].append(mat[i][j])
    vals = [val for key, val in mp.items()]
    return vals
def diagonal2(mat):

    n , m = len(mat), len(mat)
    mp = defaultdict(list)
    for i in range(n):
        for j in range(m):
            mp[(i - j)].append(mat[i][j])
    vals = [val for key, val in mp.items()]
    return vals
 
def solve():
    n = it()
    mat = [li() for _ in range(n)]
    verti = columns(mat)
    ind = n // 2
    midC = verti[ind]
    midR = mat[ind]
    Ds = diagonal(mat)
    midD = Ds[len(Ds) // 2]
    D2 = diagonal2(mat)
    midD2 = D2[0]

    sm = sum(midC) - midC[len(midC)//2] + sum(midR) - midR[len(midR) // 2] + sum(midD) - midD[len(midD)//2]+ sum(midD2) - midD2[len(midD2) // 2]
    print(sm + midR[len(midR) // 2])
    
    
 
 
t = 1
for _ in range(t):
    solve()