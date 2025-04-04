# Template Author: Lemi
import sys, heapq,math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
from math import ceil, sqrt, gcd
from random import randint

rand = randint(1, 10**5)
def ran(num): return num ^ rand
def ls(): return sys.stdin.readline().split()
def ints(): return map(int, sys.stdin.readline().split())
def strs(): return map(str, sys.stdin.readline().split())
def it(): return int(sys.stdin.readline())
def st(): return sys.stdin.readline().strip()
def li(): return list(map(int, sys.stdin.readline().split()))
def yesNo(value): return 'YES' if value == 1 else 'NO' 
 

def solve():
    n, m = ints()
    mat = [st() for _ in range(n)]

    row_count = {} 
    col_count = {}  

    total_walls = 0  
    for i in range(n):
        for j in range(m):
            if mat[i][j] == '*':
                row_count[i] = row_count.get(i, 0) + 1
                col_count[j] = col_count.get(j, 0) + 1
                total_walls += 1

    for i in range(n):
        for j in range(m):
            row_hits = row_count.get(i, 0)
            col_hits = col_count.get(j, 0)
            total_hits = row_hits + col_hits

           
            if mat[i][j] == '*':
                total_hits -= 1

            if total_hits == total_walls:
                print("YES")
                print(i + 1, j + 1)  
                return

    print("NO")

t = 1
for _ in range(t):
    solve()
