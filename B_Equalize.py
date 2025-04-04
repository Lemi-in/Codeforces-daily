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
    arr = li()
    mp = Counter()
    rand = randint(1, 10 ** 5)

    for a in arr:
        mp[a ^ rand] += 1
    st = [key ^ rand for key, val in mp.items()]
    st.sort()
    pnt = 0  
    ans = 1  

    for i in range(1, len(st)):
        if st[i] - st[pnt] < n:
            ans += 1
        else:
            pnt += 1
    
    print(ans)


t = it()
for _ in range(t):
    solve()
