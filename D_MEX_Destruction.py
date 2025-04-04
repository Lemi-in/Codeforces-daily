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

#this better work
def solve():
    n = it()
    arr = li()
    if sum(arr) == 0:
        print(0)
        return
    l = 0
    while l < n:
        while arr[l] == 0:
            l += 1
        break
    if arr[l:].count(0) == 0:
        print(1)
        return
    
    r = n - 1
    while r > 0:
        while arr[r] == 0:
            r -= 1
        break
    if arr[:r + 1].count(0) == 0:
        print(1)
        return
    l , r = 0 , n - 1
    while l < r:
        while l < r and arr[l] == 0:
            l += 1
        while r > 0 and  arr[r] == 0:
            r -= 1
        break
    if arr[l:r + 1].count(0) == 0:
        print(1)
        return
    if arr.count(0) == 0:
        print(1)
        return
    
    print(2)


    



 
t = it()
for _ in range(t):
    solve()