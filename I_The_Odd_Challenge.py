# Template Author: Lemi
from itertools import accumulate
import sys, heapq,math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
from math import ceil, sqrt, gcd
from random import randint

def ls(): return sys.stdin.readline().split()
def ints(): return map(int, sys.stdin.readline().split())
def strs(): return map(str, sys.stdin.readline().split())
def it(): return int(sys.stdin.readline())
def st(): return sys.stdin.readline().strip()
def li(): return list(map(int, sys.stdin.readline().split()))
def yesNo(value): return 'YES' if value == 1 else 'NO' 
 
def solve():
    n , m = ints()
    arr = li()
    prefix = [0]+ list(accumulate(arr))
    for _ in range(m):
        l , r , k = ints()
        sum1 = (prefix[-1] - (prefix[r] -prefix[l-1]))%2
        sum2 = (k * (r - l +1)) %2

        if sum1 != sum2:
            print("YES")
        else:
            print("NO") 

 
 
t = it()
for _ in range(t):
    solve()