# Template Author: Lemi
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
    
    arr.sort()
    
    prefix = [0] * n
    suffix = [0] * (n + 1)
    
    
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]
    

    for i in range(n - 1, -1, -1):
        suffix[i] = suffix[i + 1] + arr[i]
    
    min_cost = float('inf')
    best_index = 0
    
    for i in range(n):
        cost = (i * arr[i] - prefix[i]) + (suffix[i + 1] - (n - i - 1) * arr[i])
        
        if cost < min_cost:
            min_cost = cost
            best_index = i
    if n % 2 == 0:
        print(arr[best_index - 1])
    else:
        print(arr[best_index])

t = 1
for _ in range(t):
    solve()
