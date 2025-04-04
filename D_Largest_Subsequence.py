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
    if list(s) == sorted(s):
        print(0)
        return
    stack = []
    rem = []


    for c in s:
        while stack and stack[-1] < c:
            rem.append(stack.pop()) 
        stack.append(c)

    

    print('inc')
    print(rem[::-1])
    print(stack)
    # temp = sorted(stack)
    # print(temp)
    

    # if temp and temp[-1][1] == n - 1:
    #     print(-1)
        


  
 
 
t = it()
for _ in range(t):
    solve()

