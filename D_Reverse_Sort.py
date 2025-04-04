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
    s = list(s)


    if s == sorted(s): 
        print(0)
        return

    indices = []
    left, right = 0, n - 1

   
    while left < right:
        while left < n and s[left] == '0':
            left += 1
        while right >= 0 and s[right] == '1':
            right -= 1
        if left < right:
            indices.append(left + 1)
            indices.append(right + 1)
            left += 1
            right -= 1

    print(1) 
    print(len(indices), *sorted(indices))

t = it()
for _ in range(t):
    solve()
