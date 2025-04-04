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
    n = it()
 
    pairs = list(zip(li(), li()))
    pairs.sort(key=lambda x: [x[1], x[0]])
    
    pos = [x[0] for x in pairs]
    ans = -sum(pos[i] * (n - i) for i in range(n))
    
    pos.sort()
    ans += sum(pos[i] * (i + 1) for i in range(n))
    print(ans)

t = 1
for _ in range(t):
    solve()