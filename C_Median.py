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
    n , x = ints()
    arr = li()
    arr.sort()
    mid = n // 2
    midean = -1

    
    if n % 2 == 0:
        if x == arr[mid - 1]:
            print(0)
            return
        else:
            midean = arr[mid - 1]

    if n % 2 != 0:
        if x == arr[mid]:
            print(0)
            return
        else:
            midean = arr[mid]

    if x < midean:
        less = 0
        for a in arr[:mid]:
            if a <= x:
                less += 1
        print(n - less - less)
        
    else:
        more = 0
        huala = arr[mid:]
        for a in huala[::-1]:
            if a >= x:
                more += 1

        print(n - more - more + 1)


t = 1
for _ in range(t):
    solve()
