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


def merge(l, r):
    global k, ans
    if k == 0 or l + 1 == r:
        return
    m = (l + r) // 2
    k -= 1
    ans[m - 1], ans[m] = ans[m], ans[m - 1]
    merge(l, m)
    merge(m, r)

def solve():
    global k, ans
    n, k = ints()
    if k % 2 == 0:
        print(-1)
        return
    
    ans = list(range(1, n + 1))
    k //= 2
    merge(0, n)

    if k:
        print(-1)
    else:
        print(*ans)
t = 1
for _ in range(t):
    solve()