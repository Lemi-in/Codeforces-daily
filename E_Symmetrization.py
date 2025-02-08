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

def findSides(matrix, i, j):
    n, m = len(matrix), len(matrix[0])
    reflections = {
        "Top-Bottom": (n - 1 - i, j),
        "Left-Right": (i, m - 1 - j),
        "Main-Diagonal": (j, i),
        "Anti-Diagonal": (n - 1 - j, m - 1 - i)
    }
    ref = {
        key: matrix[x][y] for key, (x, y) in reflections.items() if 0 <= x < n and 0 <= y < m
    }
    vals = [val for val in ref.values()]
    
    return vals

def solve():
    n = it()
    mat = [list(s()) for _  in range(n)]

    m = n
    ans = []
    for i in range(n):
        for j in range(m):
            ans.append(findSides(mat, i, j))
   
    cnt = 0
    for a in ans:
        ones = a.count('1')
        zeros = a.count('0')
        mx = max(ones, zeros)
        cnt += 4 - mx
    print(cnt // 4)

    
 
t = it()
for _ in range(t):
    solve()