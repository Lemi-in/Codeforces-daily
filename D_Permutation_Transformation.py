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
 


def build(l, r, a, d, curD=0):
    if r < l:
        return
    if l == r:
        d[l] = curD
        return
    m = max(range(l, r + 1), key=lambda i: a[i])  # Find the index of the max element
    d[m] = curD
    build(l, m - 1, a, d, curD + 1)
    build(m + 1, r, a, d, curD + 1)

def solve():
    n = it()
    a = li()
    d = [0] * n
    build(0, n - 1, a, d)
    print(*d)

t = it()
for _ in range(t):
    solve()
