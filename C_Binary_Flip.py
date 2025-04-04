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
    a = st()
    b = st()
    
    pref = [0]*n
    for i in range(n):
        if a[i] == '0':
            pref[i] -= 1
        else:
            pref[i] = 1
        pref[i] += pref[i-1]

    flag = True
    for i in range(n-1,-1,-1):
        if flag and a[i] == b[i]:
            continue
        elif not flag and a[i] != b[i]:
            continue
        elif flag and a[i] != b[i]:
            if pref[i] != 0:
                return 'NO'
            flag = False
        elif not flag and a[i] == b[i]:
            if pref[i] != 0:
                return 'NO'
            flag = True

    return 'YES'

        

 
t = it()
for _ in range(t):
    print(solve())