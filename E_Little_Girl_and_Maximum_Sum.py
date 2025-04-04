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
    n , q = ints()
    arr = li()
    query = []
    for _ in range(q):
        l , r = ints()
        query.append((l - 1 , r - 1))
    

    diff = [0] * (n + 2)
    for l , r in query:
        diff[l] += 1
        diff[r + 1] -= 1
    for i in range(1, len(diff)):
        diff[i] += diff[i - 1]
    diff.sort(reverse=True)
    arr.sort(reverse=True)
    total = 0
    for i in range(n):
        total += arr[i] * diff[i]
    print(total)
        
    
    



 
t = 1
for _ in range(t):
    solve()