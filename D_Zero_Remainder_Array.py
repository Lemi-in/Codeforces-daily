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
    n,k= ints()
    arr= li()
    h=defaultdict(int)
    zero=[]
    for i in arr:
        zero.append(i%k)
        x=(k-i)%k
        if x:
            if h[x]==0:
                h[x]=x+1
            else:
                h[x]+=k
    if max(zero)==0:
        print(0)
    else:
        print(max(h.values()))
  
 
 
t = it()
for _ in range(t):
    solve()