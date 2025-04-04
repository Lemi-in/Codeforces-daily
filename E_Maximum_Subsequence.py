#author: Lemi
import sys, heapq, math
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
    a = li()
    
    ans = 0
    n1 = n // 2
    
    x, y = [], []
    
    def dfs(i, goal, total, res):
        if i == goal:
            res.append(total)
            return
        dfs(i + 1, goal, total, res)
        dfs(i + 1, goal, (total + a[i]) % m, res)
    
    dfs(0, n1, 0, x)
    dfs(n1, n, 0, y)
    
    x.sort()
    y.sort()
    
    i = len(y) - 1
    for val in x:
        ans = max(ans, (val + y[-1]) % m)
        while i >= 0 and (val + y[i]) >= m:
            i -= 1
        if i >= 0:
            ans = max(ans, (val + y[i]) % m)
    
    print(ans)

t = 1
for _ in range(t):
    solve()
