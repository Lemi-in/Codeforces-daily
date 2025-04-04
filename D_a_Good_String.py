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

def calc(s, c):
    if len(s) == 1:
        return int(s[0] != c)
    mid = len(s) // 2
    cntl = calc(s[:mid], chr(ord(c) + 1))
    cntl += mid - s[mid:].count(c)
    cntr = calc(s[mid:], chr(ord(c) + 1))
    cntr += mid - s[:mid].count(c)
    return min(cntl, cntr)

def solve():
    n = it()
    s = st()
    print(calc(s, 'a'))

t = it()
for _ in range(t):
    solve()
