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
    s = st()
    n = len(s)
    m = it()
    mp = [0] * n
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            mp[i] += 1
    pref = [0] * (n )
    for i in range(1,n):
        pref[i] = pref[i - 1] + mp[i - 1]
 
    for _ in range(m):
        l , r = ints()
        l , r = l - 1, r - 1
        print(pref[r] - pref[l])


    
 
 
t = 1
for _ in range(t):
    solve()