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
    la, lb = ints()
    a = li()
    b = li()

    pos = defaultdict(lambda: -1)
    
    for i, num in enumerate(b):
        pos[num] = i

    ans, cur, r = 0, 0, 0

    for i in range(la):
        if r < i:
            r = i
            cur = 0
        elif i > 0:
            ncur = pos[a[i]] - pos[a[i - 1]]
            if ncur < 0:
                ncur += lb
            cur -= ncur

        if pos[a[i]] == -1:
            continue

        while r < i + la - 1:
            nxt = (r + 1) % la
            if pos[a[nxt]] == -1:
                break
            ncur = pos[a[nxt]] - pos[a[r % la]]
            if ncur < 0:
                ncur += lb
            if cur + ncur >= lb:
                break
            r += 1
            cur += ncur

        ans = max(ans, r - i + 1)

    print(ans)
t = 1
for _ in range(t):
    solve()
