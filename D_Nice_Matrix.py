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
 


def cost(values, target):
    return sum(abs(x - target) for x in values)

def calculate(mat, n, m):
    total = 0
    
    for i in range((n + 1) // 2):
        for j in range((m + 1) // 2):
            values = []
            seen = set()
            
            if (i, j) not in seen:
                values.append(mat[i][j])
                seen.add((i, j))
            
            if (i, m - 1 - j) not in seen:
                values.append(mat[i][m - 1 - j])
                seen.add((i, m - 1 - j))
            
            if (n - 1 - i, j) not in seen:
                values.append(mat[n - 1 - i][j])
                seen.add((n - 1 - i, j))
            
            if (n - 1 - i, m - 1 - j) not in seen:
                values.append(mat[n - 1 - i][m - 1 - j])
                seen.add((n - 1 - i, m - 1 - j))
            
            left = min(values)
            right = max(values)
            
            while left < right:
                mid = (left + right) // 2
                cost_mid = cost(values, mid)
                cost_mid_plus_1 = cost(values, mid + 1)
                
                if cost_mid <= cost_mid_plus_1:
                    right = mid
                else:
                    left = mid + 1

            total += cost(values, left)
    
    return total

def solve():
    n, m = ints()
    mat = [li() for _ in range(n)]
    print(calculate(mat, n, m))

if __name__ == "__main__":
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()
