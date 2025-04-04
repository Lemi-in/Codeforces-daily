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
    cnt = 0
    neg = 0
    pos = 0
    for a in arr:
        if a == 0:
            cnt += 1
        elif a > 0:
            pos += 1
        else:
            neg += 1
    op = 0
    for i in range(n):
        if arr[i] < 0:
            op += abs(arr[i]) - 1
            arr[i] = -1
        elif arr[i] > 0:
            op += arr[i] - 1
            arr[i] = 1
        else:
            op += 1
            arr[i] = 1
    if neg % 2 == 0:
        print(op)
    else:
        if cnt > 0:
            print(op)
        else:
            print(op + 2)
   


 
 
t = 1
for _ in range(t):
    solve()