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
    s = st()
    odd = [l for l in s if int(l) % 2 != 0]
    even = [l for l in s if int(l) % 2 == 0]
    ans = []
    l , r = 0 , 0 
    while l < len(odd) and r < len(even):
        if odd[l] < even[r]:
            ans.append(odd[l])
            l += 1
        else:
            ans.append(even[r])
            r += 1
    ans.extend(odd[l:])
    ans.extend(even[r:])
    print(''.join(ans))


t = it()
for _ in range(t):
    solve()