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
    n , k = ints()
    a = li()
    b = li()
    brr = [[a[i],i] for i in range(n)]
    arr = [[b[i],i] for i in range(n)]
    arr.sort()
    brr.sort()

    for i in range(n):
        arr[i][1] = brr[i][1]
    arr.sort(key=lambda x : x[1])
    arr = [arr[i][0] for i in range(n)]
    print(*arr)
    

    
    

 
 
t = it()
for _ in range(t):
    solve()