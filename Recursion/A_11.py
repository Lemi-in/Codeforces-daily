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
def fib():
    arr = [1] * (1000)
    for i in range(2,1000):
        arr[i] = arr[i - 1] + arr[i - 2]
    return arr
 
def solve():
    n = it()
    arr = fib()
    s = ''
    for i in range(1, n + 1):
        if i in arr:
            s += 'O'
        else:
            s += 'o'
    print(s)

 
 
t = 1
for _ in range(t):
    solve()