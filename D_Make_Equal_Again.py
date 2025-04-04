# Template Author: Lemi
import sys, heapq,math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
from math import ceil, sqrt, gcd
from random import randint

rand = randint(1, 10**5)
def ran(num): return num ^ rand
def ls(): return sys.stdin.readline().split()
def ints(): return map(int, sys.stdin.readline().split())
def strs(): return map(str, sys.stdin.readline().split())
def it(): return int(sys.stdin.readline())
def st(): return sys.stdin.readline().strip()
def li(): return list(map(int, sys.stdin.readline().split()))
def yesNo(value): return 'YES' if value == 1 else 'NO' 
 


def solve():
    n = it()
    arr = li()
    
    if arr[0] == arr[-1]:
        left = 0
        while left < n and arr[left] == arr[0]:
            left += 1

        right = 0
        while right < n and arr[n - 1 - right] == arr[0]:
            right += 1

        print(max(0, n - (left + right)))
    else:
        left = 0
        while left < n and arr[left] == arr[0]:
            left += 1

        right = 0
        while right < n and arr[n - 1 - right] == arr[-1]:
            right += 1

        print(min(n - left, n - right))

t = it()
for _ in range(t):
    solve()
