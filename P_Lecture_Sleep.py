# Template Author: Lemi
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
    arr = li()
    time = li()

    awake = sum(arr[i] for i in range(n) if time[i] == 1)
    asleep = [arr[i] if time[i] == 0 else 0 for i in range(n)]
    
    mx = 0
    cur = sum(asleep[:k])
    mx = cur
    l = 0

    for r in range(k, n):
        cur += asleep[r]
        cur -= asleep[l]
        mx = max(mx, cur)
        l += 1

    print(awake + mx)

t = 1
for _ in range(t):
    solve()
