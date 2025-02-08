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
    n , m = ints()
    mat = [list(s()) for _ in range(n)]
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for i in range(n):
        for j in range(m):
            if mat[i][j] == '.':  
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m and mat[ni][nj] == '*':
                        print("NO")
                        return
            elif mat[i][j].isdigit():  
                bombs = int(mat[i][j])
                cnt = 0
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m and mat[ni][nj] == '*':
                        cnt += 1
                if cnt != bombs:
                    print("NO")
                    return

    print("YES")
 
 
t = 1
for _ in range(t):
    solve()
