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


def solve():
    st = s()
    l = 0
    arr = list(st)
    n = len(arr)
    turn = True
    for i in range(n):
        if arr[i] == '?':
            if turn:
                arr[i] = '0'
                turn = False
            else:
                arr[i] = '1'
                turn = True
    
    def count(arr):
        n = len(arr)
        count = 0
        length = 1

        for i in range(1, n):
            if arr[i] == '?' or arr[i] != arr[i - 1]:
                length += 1
            else:
                count += (length * (length + 1)) // 2
                length = 1

        count += (length * (length + 1)) // 2

        # Subtract cases where '?' is alone
        for i in range(n):
            if arr[i] == '?' and (i == 0 or arr[i - 1] != '?') and (i == n - 1 or arr[i + 1] != '?'):
                count -= 1

        return count

    print(count(['0','?','1','0']))
    # print(count(arr))
   

t = it()
for _ in range(t):
    solve()