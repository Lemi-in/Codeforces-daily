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
 


def pref(arr):
    mx = 0
    curr = 0
    for num in arr:
        curr += num
        mx = max(mx, curr)
    return mx

def solve():
    n = it()
    r = li()
    m = it()
    b = li()

    max_r = pref(r)
    max_b = pref(b)
    
    print(max(0, max_r + max_b))

t = it()
for _ in range(t):
    solve()
