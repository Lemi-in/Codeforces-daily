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
    w, h, n = ints()

    fac = 1
    while w % 2 == 0:
        w //= 2
        fac *= 2
    while h % 2 == 0:
        h //= 2
        fac *= 2

    print("YES" if fac >= n else "NO")
t = it()
for _ in range(t):
    solve()