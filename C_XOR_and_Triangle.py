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

def ye2Bizet(num):
    return num & (num - 1) == 0 or num & (num + 1) == 0

def solve():
    num = it()

    if ye2Bizet(num):
        print(-1)
        return
    
    sett, unset = 0, 0
    while (num >> sett) & 1 == 0:
        sett += 1
    while (num >> unset) & 1 == 1:
        unset += 1

    print((1 << sett) | (1 << unset))

t = it()
for _ in range(t):
    solve()
