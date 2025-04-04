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
    s = st()
    
    zero = deque()
    one = deque()
    ans = [0] * n
    subCnt = 0  
    
    for i in range(n):
        if s[i] == '0':  
            if one:
                indx = one.popleft()
            else:
                subCnt += 1
                indx = subCnt
            
            ans[i] = indx
            zero.append(indx)
        else:
            if zero:
                indx = zero.popleft()
            else:
                subCnt += 1
                indx = subCnt
            
            ans[i] = indx
            one.append(indx)

    print(subCnt)
    print(*ans)

t = it()
for _ in range(t):
    solve()
