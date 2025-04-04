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
    
    sortd = sorted(arr)
    if arr == sortd:
        print(0)
        return
    
    def op1(a):
        res = a[:]
        for i in range(0, 2 * n, 2):
            res[i], res[i + 1] = res[i + 1], res[i]
        return res

    def op2(a):
        return a[n:] + a[:n]
    

    step1 = 0
    original = arr[:]

    for _ in range(2 * n):
        if arr == sortd:
            break
        arr = op1(arr) if step1 % 2 == 0 else op2(arr)
        step1 += 1
    cnt = 0
    if arr != sortd:
        step1 = float('inf')
        cnt += 1
    arr = original
    step2 = 0
    for _ in range(2 * n):
        if arr == sortd:
            break
        arr = op2(arr) if step2 % 2 == 0 else op1(arr)
        step2 += 1
    if arr != sortd:
        step2 = float('inf')
        cnt += 1
    if cnt == 2:
        print(-1)
    else:
        print(min(step1, step2))

solve()
