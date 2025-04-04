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
    n, k = ints()
    if n == 1:
        print(1)
        print(1)
        return
    if k == n or k == 1:
        print(-1)
        return
    if (k - 1) % 2 == 0:
        print(5)
        print(1, (k - 1), k, k + 1, k + 2)
        return
    print(3)
    print(1, k, k + 1)
 

t = it()
for _ in range(t):
    solve()
