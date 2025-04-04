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
 

def sub(s, t):
    l, r = 0, 0
    temp = []
    while l < len(s) and r < len(t):
        if s[l] == t[r] or s[l] == '?':
            if s[l] == '?':
                temp.append(t[r])
            r += 1
        l += 1
    return [temp,r == len(t)]

def change(s, t, c):
    s = list(s)  
    indx = 0


    for i in range(len(s)):
        if s[i] == '?' and indx < len(c):
            s[i] = c[indx]
            indx += 1

    for i in range(len(s)):
        if s[i] == '?':
            s[i] = 'a' 
    return ''.join(s)

def solve():
    s = st()
    t = st()
    sb = sub(s,t)
    c = sb[0]
    if sb[1]:
        print("YES")
        print(change(s, t, c))
    else:
        print('NO')
       


t = it()
for _ in range(t):
    solve()
