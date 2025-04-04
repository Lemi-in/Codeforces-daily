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
    idx = [(i + 1, arr[i]) for i in range(n)]
    idx.sort(key=lambda x: x[1])
    key = [x for x , y in idx]

    ans = ['0'] * (n + 1)
    mx = key[0]
    mn = key[0]
    ans[0] = '1'
    for i in range(1, n):
        mx = max(mx, key[i])
        mn = min(mn, key[i])
        if mx - mn <= i:
            ans[i] = '1'
    ans.pop()
    print(''.join(ans))
        




   
 
 
t = it()
for _ in range(t):
    solve()



#  left, right = n + 1, 0
#     result = ['0'] * n
#     seen = set()

#     for i in range(n):
#         seen.add(arr[i])
#         left = min(left, arr[i])
#         right = max(right, arr[i])

#         if right - left + 1 == i + 1 and len(seen) == i + 1:
#             result[i] = '1'

#     print(''.join(result))