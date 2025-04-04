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

    mn = 0
    left, right = 0, 0

    for i in range(n):
        greaterZan = 0
        lessZan = 0
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                greaterZan += 1
            elif arr[j] < arr[i]:
                lessZan += 1

            curr = greaterZan - lessZan
            if curr < mn:
                mn = curr
                left = i
                right = j

    print(left + 1, right + 1)


t = it()
for _ in range(t):
    solve()
