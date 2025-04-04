# author: Lemi
import sys, heapq, math
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


dp = [0] * (200001)

def greedy(num):
    cnt = 0
    while num > 0:
        num //= 3
        cnt += 1
    return cnt


for i in range(1, 200001):
    dp[i] = greedy(i)

pref = dp[:]

for i in range(1, 200001):
    pref[i] += pref[i - 1] 

def solve():
    l, r = ints()
    print((pref[r] - pref[l]) + dp[l] + dp[l])

t = it()
for _ in range(t):
    solve()
