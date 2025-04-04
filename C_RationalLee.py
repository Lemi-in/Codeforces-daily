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
    n,k = ints()
    a = sorted(li())
    b = sorted(li() , reverse=True)
    ans = 0
    i = 0
    j = n-1
    x = len(b)-1
    i = 0
    j = n-1
    while k > 0 and b[x] == 1:
        ans += a[j]*2
        x-=1
        j-=1
        k-=1

    x = 0
    while k>0:
        ans+=(a[i]+a[j])
        j-=1
        i+=(b[x]-1)
        k-=1
        x+=1

    print(ans)

t = it()
for _ in range(t):
    solve()