
#author: Lemi
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
    n , m  = ints()
    graph = defaultdict(list)

    for _ in range(m):
        u, v = ints()
        graph[u].append(v)
        graph[v].append(u)
        
    degrees = [0] * (n + 1)
    for node in graph:
        degrees[node] = len(graph[node])

    if m == n - 1:  
        endpoints = degrees.count(1)
        if endpoints == 2 and degrees.count(2) == n - 2:
            print("bus topology")
        elif endpoints == n - 1 and degrees.count(n - 1) == 1:
            print("star topology")
        else:
            print("unknown topology")
    elif m == n: 
        if degrees.count(2) == n:
            print("ring topology")
        else:
            print("unknown topology")
    else:
        print("unknown topology")
    


t = 1
for _ in range(t):
    solve()


