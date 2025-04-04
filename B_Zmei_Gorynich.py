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
    n , x = ints()
    arr = [list(ints()) for _ in range(n)]

    cnt = 0
    if all(h >= d for d , h in arr):
        print(-1)
        return
    mn = float('inf')
    l , k = -1 , -1
    print('this')
    for d , h in arr:
        if d > h:
            print((x // (d - h)))
        if d > h:
            if x - d + h < mn:
                mn = x - d + h
                l , k = d , h
    # print(l,k)
    # print(math.ceil(x / (l - k)))
# 5 , 1000000000
# [[2, 1], [1, 10], [1, 1], [4, 1000000000], [3, 3]]


# 3 ,1000000000
# [[1231, 1200], [1000, 800], [1, 100]]

 
 
t = it()
for _ in range(t):
    solve()