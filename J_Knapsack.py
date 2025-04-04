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
    n, w = ints()
    arr = [list(ints()) for _ in range(n)]
    weight = [a[0] for a in arr]
    value = [a[1] for a in arr]

    mx = 0
    def backtrack(i,  sm, weight, value, limit, w):
        nonlocal mx
        if i <= len(weight) and limit <= w:
            mx = max(mx, sm)
        
        
        for j in range(i,len(weight)):
            sm += value[j]
            limit += weight[j]
            backtrack(j + 1, sm, weight, value, limit, w)
            sm -= value[j]
            limit -= weight[j]
        
    
    backtrack(0, 0,weight, value, 0, w)
    print(mx)
    
t = 1
for _ in range(t):
    solve()
