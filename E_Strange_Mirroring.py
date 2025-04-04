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


def helper(n, k, s):
    if n == 1:
        return s[n - 1]
    
    length = (1 << n) - 1 
    mid = (length // 2) + 1  
    
    if k == mid:
        return s[n // 2]
    elif k < mid:
        return helper(n - 1, k , s )
    else:
        char = helper(n - 1, length - k + 1, s)
        if char.isupper():
            return char.lower()
        else:
            return char.upper()


def solve():
    s = st()
    m = len(s)
    n = it()
    query = li()
    for q in query:
        print(helper(m, q - 1,s),end=' ')
    
    print('')
    

 
t = it()
for _ in range(t):
    solve()