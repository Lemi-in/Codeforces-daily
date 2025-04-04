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


def backtrack(i, store, ans, n):
    if i == n:
        ans.append(store[:])
        return
    store.append(0)
    backtrack(i + 1, store, ans, n)
    store.pop()
    
    store.append(1)
    backtrack(i + 1, store, ans, n)
    store.pop()

def solve():
    n = it()
    ans = []
    backtrack(0, [], ans, n)
    for arr in ans:
        print(''.join([str(i) for i in arr]))
    
t = it()
for _ in range(t):
    solve()
