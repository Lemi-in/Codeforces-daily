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
    n = it()
    l = li()
    s = li()

    cnt=0

    mp = {}
    pos=[0 for x in range(n)]

    for i in range(n):
        mp[s[i]] = i+1

    for i in range(n):
        pos[i] = mp[l[i]]

    mx  = pos[0]
    for i in range(1,n):
        if(mx > pos[i]):
            cnt+=1
        mx = max(mx ,pos[i])

    print(cnt)    

 
t = 1
for _ in range(t):
    solve()