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
    arr = li()
    
    prefix = [0] * n
    prefix[0] = arr[0]
    
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]

    q = deque()

    for i in range(n):
        while q and arr[q[-1]] <= arr[i]:
            idx = q.pop()
            new = prefix[i]
            if idx:
                new -= prefix[idx - 1]
            if new > arr[i]:
                print("NO")
                return
        q.append(i)

    arr.reverse()


    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]

    q.clear()

    for i in range(n):
        while q and arr[q[-1]] <= arr[i]:
            idx = q.pop()
            new = prefix[i]
            if idx:
                new -= prefix[idx - 1]
            if new > arr[i]:
                print("NO")
                return
        q.append(i)

    print("YES")
    
t = it()
for _ in range(t):
    solve()
