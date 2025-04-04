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
    a, b, c = ints()
    m = it()

    v = []
    for _ in range(m):
        price, type_ = input().split()
        v.append((int(price), type_))

    v.sort()

    ans = 0
    cnt = 0

    for price, type_ in v:
        if a and type_ == "USB":
            a -= 1
            cnt += 1
            ans += price
        elif b and type_ == "PS/2":
            b -= 1
            cnt += 1
            ans += price
        elif c:
            c -= 1
            cnt += 1
            ans += price

    print(cnt, ans)

 
 
t = 1
for _ in range(t):
    solve()
