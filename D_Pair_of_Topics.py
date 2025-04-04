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
 
def lb(arr,d):
    left,right=0,len(arr)
    while left<right:
        mid=(left+right)//2
        if arr[mid]<d:
            left=mid+1
        else:
            right=mid
    return left

def solve():
    n = it()
    arr = li()
    b = li()
    c=  []
    for i in range(n):
        c += [arr[i] - b[i]]
    c.sort()
    ans=0
    for i in range(n):
        if c[i] <= 0:
            continue
        p = lb(c,-c[i]+1)
        ans += i- p
    print(ans)
    
t=1
#t=int(input())
for i in range(t):
    solve()