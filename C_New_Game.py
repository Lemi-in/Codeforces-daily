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
    arr = li()
    arr.sort()
    
    ans = 0
    right = 0
    for left in range(n):
        right = max(right, left)
        while right + 1 < n and arr[right + 1] <= arr[right] + 1 and arr[right + 1] < arr[left] + k:
            right += 1
        ans = max(ans, right - left + 1)
    print(ans)
 
 
t = it()
for _ in range(t):
    solve()