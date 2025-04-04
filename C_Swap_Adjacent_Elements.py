# Template Author: Lemi
import sys, heapq,math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
from math import ceil, sqrt, gcd
from random import randint

def ls(): return sys.stdin.readline().split()
def ints(): return map(int, sys.stdin.readline().split())
def strs(): return map(str, sys.stdin.readline().split())
def it(): return int(sys.stdin.readline())
def s(): return sys.stdin.readline().strip()
def li(): return list(map(int, sys.stdin.readline().split()))
def yesNo(value): return 'YES' if value == 1 else 'NO' 
 
def solve():
    n = it()

    a = li()
    s = input()
    s += '0'

    p1 = 0
    for i in range(n):
        if s[i] == '0':
            a[p1:i+1] = sorted(a[p1:i+1])
            p1 = i + 1

    for i in range(1, n):
        if a[i - 1] > a[i]:
            print("NO")
            return 

    print("YES")

 
 
t = 1
for _ in range(t):
    solve()
