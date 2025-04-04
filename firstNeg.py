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
 

arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
n = len(arr)

q = deque()

ans = []
l = 1
for i in range(k):
    if arr[i] < 0:
        q.append(i)
if q:
    ans.append(arr[q[0]])
else:
    ans.append(0)

for r in range(k,n):
    if arr[r] < 0:
        q.append(r)
    while q and l > q[0]:
        q.popleft()
    if q:
        ans.append(arr[q[0]])
    else:
        ans.append(0)
        

    l += 1

print(ans)

