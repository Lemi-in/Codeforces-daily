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

def mx(arr):
    if not arr:
        return 0

    n = len(arr)
    result = 0
    current = arr[0]

    for i in range(1, n):
        # Check if the sign alternates
        if (arr[i] > 0 and current < 0) or (arr[i] < 0 and current > 0):
            result += current
            current = arr[i]
        else:
            # Update current to the maximum value of the same sign
            current = max(current, arr[i], key=abs)

    # Add the last element
    result += current
    return result

 
def solve():
    n = it()
    arr = li()
    print(mx(arr))
 
 
t = it()
for _ in range(t):
    solve()