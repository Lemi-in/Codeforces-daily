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
    n , m = ints()
    arr = li()
    right = [0] * n
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            right[i] = arr[i] - arr[i + 1]
    right.insert(0,0)
    for i in range(1,len(right)):
        right[i] += right[i - 1]
    right.pop()

    left = [0] * n
    temp = arr.reverse()
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            left[i] = arr[i] - arr[i + 1]
    
    left.reverse()
    left.append(0)
    for i in range(1, len(left)):
        left[i] += left[i - 1]
    left.pop()
    print(left)


    for _ in range(m):
        l , r = ints()
        l , r = l - 1, r - 1
        if l < r:
            print(right[r] - right[l])
        else:
            print(left[l] - left[r])
        
    

t = 1
for _ in range(t):
    solve()