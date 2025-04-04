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
    n, k = ints()
    arr = li()
    
    mp = Counter()
    rand = randint(1, 10 ** 5)
    
    for a in arr:
        mp[a ^ rand] += 1
    st = [key ^ rand for key, val in mp.items() if val >= k]
    st.sort()
    

    if not st:
        print(-1)
        return


    l = 0
    mx = -1
    x, y = -1, -1

    for r in range(len(st)):
        if r > 0 and st[r] - st[r - 1] > 1:
            l = r  
        if st[r] - st[l] > mx:
            mx = st[r] - st[l]
            x, y = st[l], st[r]
    if x == -1 or y == -1:
        print(-1)
    else:
        print(x, y)

t = it()
for _ in range(t):
    solve()