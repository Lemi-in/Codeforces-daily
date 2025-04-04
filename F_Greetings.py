#author: Lemi
import sys, heapq,math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
from math import ceil, sqrt, gcd
from random import randint
from sortedcontainers import SortedList

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
    arr = [tuple(ints())[::-1] for _ in range(n)]
    arr.sort()

    ans = 0
    st = SortedList()

    for first, second in arr:
        ans += len(st) - st.bisect_left(second)
        st.add(second)

    print(ans)

t = it()
for _ in range(t):
    solve()
