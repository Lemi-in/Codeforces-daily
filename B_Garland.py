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
    s = st()
    t = st()
    freqS = [0] * 26
    freqT = [0] * 26
    for c in s:
        freqS[ord(c) - ord('a')] += 1
    for c in t:
        freqT[ord(c) - ord('a')] += 1
    

    cnt = 0
    for c in t:
        if freqS[ord(c) - ord('a')] == 0:
            print(-1)
            return
    for i in range(26):
        cnt += min(freqS[i], freqT[i])
        

    print(cnt)
 
 
t = 1
for _ in range(t):
    solve()