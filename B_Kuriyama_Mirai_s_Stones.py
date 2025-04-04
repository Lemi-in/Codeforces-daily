#author: Lemi
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

def prefix(arr):
    n = len(arr)
    for i in range(1, n):
        arr[i] += arr[i - 1]
    arr.insert(0,0)
    return arr
 
def solve():
    n = it()
    v = li()

    pref = prefix(v[:])
    suff = prefix(sorted(v[:]))
    
    m = it()
    for _ in range(m):
        t , l , r = ints()
        if t == 1:
            print(pref[r] - pref[l - 1])
        else:
            print(suff[r] - suff[l - 1])
 
t = 1
for _ in range(t):
    solve()