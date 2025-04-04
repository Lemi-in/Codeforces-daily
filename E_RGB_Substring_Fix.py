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
 
def solve():
    n , k = ints()
    s = st()
   
    pattern = "RGB" * ((n // 3) + 1)
    mn = float('inf')

    preR = [0] * (n + 1)
    preG = [0] * (n + 1)
    preB = [0] * (n + 1)

    for i in range(n):
        preR[i + 1] = preR[i] + (s[i] != pattern[i % 3])
        preG[i + 1] = preG[i] + (s[i] != pattern[(i + 1) % 3])
        preB[i + 1] = preB[i] + (s[i] != pattern[(i + 2) % 3])

    for i in range(n - k + 1):
        yeR = preR[i + k] - preR[i]
        yeG = preG[i + k] - preG[i]
        yeB = preB[i + k] - preB[i]
        mn = min(mn, yeR, yeG, yeB)

    print(mn)
    
 
 
t = it()
for _ in range(t):
    solve()



