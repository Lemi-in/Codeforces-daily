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
 
def solve():
    n , x = ints()
    cnt = 0
    for _ in range(n):
        s , d = strs()
        
        if s == '+':
            x += int(d)
        else:
            if x < int(d):
                cnt += 1
            else:
                x -= int(d)
    print(x, cnt)
 
 
t = 1
for _ in range(t):
    solve()