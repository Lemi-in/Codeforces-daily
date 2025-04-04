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
    a, b , c = ints()
    mx = max(a,(max(b,c)))
    
    an ,bn , cn = -1 , -1 , -1
    if a == b and b == c :
        an = 1
        bn = 1
        cn = 1
    elif a == mx and b < mx and c < mx:
        an = 0
        bn = mx - b + 1
        cn = mx - c + 1
    elif b == mx and a < mx and c < mx:
        bn = 0
        an = mx - a + 1
        cn = mx - c + 1
    elif c == mx and a < mx and b < mx:
        cn = 0
        an = mx - a + 1
        bn = mx - b + 1

    elif a == mx and b == mx and c < mx:
        an = 1
        bn = 1
        cn = mx - c + 1
    elif a == mx and c == mx and b < mx:
        an = 1
        cn = 1
        bn = mx - b + 1
    elif b == mx and c == mx and a < mx:
        bn = 1
        cn = 1
        an = mx - a + 1
    print(an , bn , cn)
    

 
 
t = it()
for _ in range(t):
    solve()