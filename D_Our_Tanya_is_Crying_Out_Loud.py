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

def greedy(x, k, A, B):
    if x == 1:
        return 0
    if k == 1:
        return (x - 1) * A
    if x < k:
        return (x - 1) * A
    if x % k == 0:
        return min(B + greedy(x // k, k, A, B), A * (x - 1))
    return min(A * (x % k) + greedy(x - (x % k), k, A, B), A * (x - 1))

def solve():
    n = it()
    k = it()
    A = it()
    B = it()
    print(greedy(n, k, A, B))

t = 1
for _ in range(t):
    solve()