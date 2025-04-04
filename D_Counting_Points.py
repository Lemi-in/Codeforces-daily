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

def total(mp):
    cnt = 0
    for intervals in mp.values():
        intervals.sort()
        start, end = intervals[0]
        x = 0
        for s, e in intervals[1:]:
            if s <= end + 1:
                end = max(end, e)
            else:
                x += end - start + 1
                start, end = s, e

        x += end - start + 1
        cnt += x

    return cnt
 

def solve():

    n, m = ints()
    center = li()
    radi = li()
    circles = [[center[i],radi[i]] for i in range(n)]

    mp = defaultdict(list)

    for c, r in circles:
        left, right = c - r, c + r

        for x in range(left, right + 1):
            dx = x - c
            diSquare = (r * r) - (dx * dx)
            if diSquare < 0:
                continue
            y = int(math.sqrt(diSquare))
            mp[ran(x)].append((-y, y))



    print(total(mp))
    

t = it()
for _ in range(t):
    solve()
