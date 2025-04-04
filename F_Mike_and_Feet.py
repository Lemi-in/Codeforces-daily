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
 

def find(arr):
    n = len(arr)
    prev = [-1] * n
    nxt = [n] * n
    stack = []

    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        prev[i] = stack[-1] if stack else -1
        stack.append(i)
    
    stack.clear()

    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        nxt[i] = stack[-1] if stack else n
        stack.append(i)

    return prev, nxt

def solve():
    n = it()
    arr = li()
    
    prev, nxt = find(arr)

    pick = [-float('inf')] * (n + 1)

    for i in range(n):
        length = nxt[i] - prev[i] - 1
        pick[length] = max(pick[length], arr[i])

    
    for i in range(n - 1, 0, -1):
        pick[i] = max(pick[i], pick[i + 1])

    print(*pick[1:])
   


t = 1
for _ in range(t):
    solve()
