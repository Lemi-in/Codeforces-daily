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
def st(): return sys.stdin.readline().strip()
def li(): return list(map(int, sys.stdin.readline().split()))
def yesNo(value): return 'YES' if value == 1 else 'NO' 
 


def solve():
    n, q = ints()
    s = st()

    pref = [[0] * 26 for _ in range(n + 1)]

    for i in range(n):
        index = ord(s[i]) - ord('a')  
        for j in range(26):
            pref[i + 1][j] = pref[i][j] + (1 if j == index else 0)

    
    for _ in range(q):
        l, r, c = strs()
        l, r = int(l) - 1, int(r)  
        index = ord(c) - ord('a')

        dirsha = (r // n) - (l // n)
        start = l % n
        end = r % n

        count = dirsha * pref[n][index]  
        count += pref[end][index]  
        count -= pref[start][index]  

        print(count)


t = it()
for _ in range(t):
    solve()
