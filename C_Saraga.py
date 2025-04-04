#author: Lemi
import sys, heapq,math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
from math import ceil, sqrt, gcd, inf
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
    s = st()
    t = st()
    
    preS = [inf] * 26
    preT = [-inf] * 26
    
    
    for i in range(len(s) - 1, 0, -1):
        preS[ord(s[i]) - ord('a')] = i

    for i in range(len(t) - 1):
        preT[ord(t[i]) - ord('a')] = i
    
    ans = inf
    best = ""
    
    for c in range(26):
        length = preS[c] + len(t) - preT[c]
        if length < ans:
            ans = length
            best = s[:preS[c]] + t[preT[c]:]
    
    print(best if ans < inf else "-1")

t = 1
for _ in range(t):
    solve()
