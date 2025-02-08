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
    mat = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, m + 1):

            if (i % 4 <= 1):  
                i_yichalal = True
            else:
                i_yichalal = False

            if (j % 4 <= 1):  
                j_yichalal = True
            else:
                j_yichalal = False

            if i_yichalal != j_yichalal:
                row.append(0)
            else:
                row.append(1)
        
        mat.append(row)
    for row in mat:
        print(*row)
t = it()
for _ in range(t):
    solve()

