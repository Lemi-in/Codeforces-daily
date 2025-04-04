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
    n = it()
    arr = li()
    freq = [0] * (max(arr) + 1)

    for a in arr:
        freq[a] += 1

    four , half = 0 , 0
    for a in freq:
        if a >= 4:
            four += (a // 4)
            half += (a % 4 >= 2)
        else:
            half += (a >= 2)

    print(four + (half // 2))


 
t = 1
for _ in range(t):
    solve()