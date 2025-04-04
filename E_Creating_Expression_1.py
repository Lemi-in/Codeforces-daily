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
 

def backtrack(i, sm):
    if i == size:
        return sm == result
    return backtrack(i + 1, sm + arr[i]) or backtrack(i + 1, sm - arr[i])

def solve():
    global size, result, arr
    size, result = ints()
    arr = li()
    
    print(yesNo(backtrack(1, arr[0])))  

t = 1
for _ in range(t):
    solve()
