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
    n, x ,y  = ints()
    arr = li()
    sm = 0
    for i in arr:
        sm += i
    arr.sort()
    left = sm - y
    right = sm - x
    count = 0

    i = n - 1
    j = n - 1

    for idx, num in enumerate(arr):
        l = left - num
        r = right - num

        while i > 0 and arr[i - 1] >= l:
            i -= 1
        while j > 0 and arr[j] > r:
            j -= 1

        if (arr[i] >= l and arr[j] <= r ):
            tmp = max(i, idx + 1)
            if (tmp <= j):
                count +=  (j - tmp + 1)

    print(max(count, 0))

 
t = it()
for _ in range(t):
    solve()
