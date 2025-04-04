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
    arr.sort()
    p = 0
    q = 2
    ans = []
    c = 0
    while(p<=n-2):
        if(p == q-1):
            q += 1
            ans.append(c)
            c = 0
        elif(arr[p] + arr[p+1] <= arr[q]):
            c += 1
            p += 1
        else:
            q += 1
            ans.append(c)
            c = 0
        if(q == n):
            break

    for b in range(len(ans) -1):
        ans[b+1] += ans[b]

    for b in range(len(ans)):
        ans[len(ans) - 1 - b] += b
        
    print(min(ans))


    
 
t = it()
for _ in range(t):
    solve()
