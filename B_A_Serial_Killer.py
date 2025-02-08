# Template Author: Lemi
import sys
import heapq
import math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
from math import ceil, sqrt, gcd

def ls(): return sys.stdin.readline().split()
def ints(): return map(int, sys.stdin.readline().split())
def strs(): return map(str, sys.stdin.readline().split())
def it(): return int(sys.stdin.readline())
def s(): return sys.stdin.readline().strip()
def li(): return list(map(int, sys.stdin.readline().split()))
 
def solve():
    killed , app = strs()
    if arr[0] == killed:
        arr[0] = app
    else:
        arr[1] = app
    print(*arr)
    
    
initial, victim = strs()
print(initial , victim)
arr = [initial, victim]
t = it()
for _ in range(t):
    solve()
