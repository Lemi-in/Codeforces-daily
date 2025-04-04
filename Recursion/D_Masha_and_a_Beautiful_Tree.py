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
 


def solve_recursive(l, r, arr):
    if r - l == 1:
        return 0
    mid = (l + r) // 2
    mal = max(arr[l:mid])
    mar = max(arr[mid:r])
    ans = 0
    if mal > mar:
        ans += 1
        arr[l:mid], arr[mid:r] = arr[mid:r], arr[l:mid]
    return solve_recursive(l, mid, arr) + solve_recursive(mid, r, arr) + ans

def solve():
    m = it()
    arr = li()
    ans = solve_recursive(0, m, arr)
    print(ans if arr == sorted(arr) else -1)

t = it()
for _ in range(t):
    solve()
