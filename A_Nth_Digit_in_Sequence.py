# Template Author: Lemi
import sys, heapq,math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
from math import ceil, sqrt, gcd
from random import randint

def ls(): return sys.stdin.readline().split()
def ints(): return map(int, sys.stdin.readline().split())
def strs(): return map(str, sys.stdin.readline().split())
def it(): return int(sys.stdin.readline())
def s(): return sys.stdin.readline().strip()
def li(): return list(map(int, sys.stdin.readline().split()))
def yesNo(value): return 'YES' if value == 1 else 'NO' 
def get(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    return digits
def solve():
    n = it()
    arr = []
    for i in range(1 , 1000):
        num = get(i)
        arr.extend(num[::-1])
    print(arr[n - 1])
    

 
 
t = 1
for _ in range(t):
    solve()