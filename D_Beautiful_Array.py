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
    n, x = ints()
    nums = li()
    
    ans = 0
    dp1, dp2, dp3 = 0, 0, 0
    for num in nums:
        dp1, dp2, dp3 = max(0, dp1) + num, max(0, dp1, dp2) + num * x, max(0, dp1, dp2, dp3) + num
        ans = max(ans, dp1, dp2, dp3)
    
    print(ans)

 
 
t = 1
for _ in range(t):
    solve()