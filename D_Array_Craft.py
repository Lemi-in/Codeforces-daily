# Template Author: Lemi
import sys, heapq,math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
from math import ceil, sqrt, gcd
from random import randint

def ls(): return sys.stdin.readline().split()
def ints(): return map(int, sys.stdin.readline().split())
def strs(): return map(str, sys.stdin.readline().split())
def it(): return int(sys.stdin.readline())
def s(): return sys.stdin.readline().strip()
def li(): return list(map(int, sys.stdin.readline().split()))
def yesNo(value): return 'YES' if value == 1 else 'NO' 

def solve():
    n, x, y = map(int, input().split())
    diff = [1] * n
    one = 1

    for i in range(y - 1, -1, -1):
        diff[i] = one
        one *= -1

    one = 1
    for i in range(x - 1, n):
        diff[i] = one
        one *= -1

    print(*diff)

t = int(input())
for _ in range(t):
    solve()
