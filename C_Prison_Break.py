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
 

def find(n, m, r, c):
    topL = (r - 1) + (c - 1)
    topR = (r - 1) + (m - c)
    botL = (n - r) + (c - 1)
    botR = (n - r) + (m - c)
    return max(topL, topR, botL, botR)

def solve():
    n, m, r, c = ints()
    print(find(n, m, r, c))

t = it()
for _ in range(t):
    solve()
