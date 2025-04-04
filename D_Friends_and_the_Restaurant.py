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
    x = li()
    y = li()

    nums = [y[i] - x[i] for i in range(n)]
    nums.sort()
    cnt = 0
    left, right = 0, n - 1
    while left < right:
        if nums[left] + nums[right] >= 0:
            cnt += 1
            right -= 1
        left += 1

    print(cnt)

 
 
t = it()
for _ in range(t):
    solve()