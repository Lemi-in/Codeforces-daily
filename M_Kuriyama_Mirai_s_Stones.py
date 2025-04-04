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

def prefix(arr):
    pref = [0] + arr.copy()
    for i in range(1, len(pref)):
        pref[i] += pref[i - 1]
    return pref

 
def solve():
    n = it()
    v = li()
    u = sorted(v)
    m = it()
    vPref = prefix(v)
    uPref = prefix(u)

    for _ in range(m):
        t , l , r = ints()
        if t == 1:
            print(vPref[r] - vPref[l - 1])
        else:
            print(uPref[r] - uPref[l - 1])
 
t = 1
for _ in range(t):
    solve()