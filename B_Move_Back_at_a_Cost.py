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
 
def solve():
    n = it()
    arr = li()
    dec = []
    inc = []

    for i in range(n):
        while dec and dec[-1] > arr[i]:
            inc.append(dec.pop() + 1)
        dec.append(arr[i])
   
    inc.sort()
    if not inc:
        print(*dec)
        return
    mn = inc[0]
    for i in range(len(dec)):
        dec[i] += (dec[i] > mn)

    print(*sorted(inc + dec))
   
t = it()
for _ in range(t):
    solve()


