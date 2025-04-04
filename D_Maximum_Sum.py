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

def find(arr):
    mx = float('-inf')
    curr = 0
    start = 0
    mxStart = 0
    mxEnd = 0

    for i in range(len(arr)):

        curr += arr[i]

        if curr > mx:
            mx = curr
        
        if curr < 0:
            curr = 0  

    return mx



def solve():
    n , k = ints()
    arr = li()
    sm = sum(arr)
    # print(find(arr))
    res = find(arr)
    if res < 0:
        print(sm % p)
        return
    ans = (res * (2**k - 1)) + sm
    print(ans % p) 
		
 
 
t = it()
for _ in range(t):
    global p
    p = 10**9 + 7
    solve()