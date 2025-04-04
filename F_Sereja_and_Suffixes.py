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
    n , m = ints()
    arr = li()
    q = [it() for _ in range(m)]
    mp1 = Counter()
    mp2 = Counter()
    for i in range(n-1 , -1 ,-1):
        mp1[arr[i]] += 1
        mp2[i + 1] = len(mp1)
    for l in q:
        print(mp2[l])
    
 
 
t = 1
for _ in range(t):
    solve()