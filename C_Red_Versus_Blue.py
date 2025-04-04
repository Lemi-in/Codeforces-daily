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
    n, r, b = ints()
    dirsha = r // (b + 1)
    keri = r % (b + 1)

    ans = []
    for i in range(b + 1):
        ans.append('R' * (dirsha + (1 if i < keri else 0)))
        if i < b:
            ans.append('B')

    print("".join(ans))

t = it()
for _ in range(t):
    solve()
