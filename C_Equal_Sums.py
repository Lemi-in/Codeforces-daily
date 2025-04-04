# Template Author: Lemi
import sys, heapq,math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
from math import ceil, sqrt, gcd

def ls(): return sys.stdin.readline().split()
def ints(): return map(int, sys.stdin.readline().split())
def strs(): return map(str, sys.stdin.readline().split())
def it(): return int(sys.stdin.readline())
def s(): return sys.stdin.readline().strip()
def li(): return list(map(int, sys.stdin.readline().split()))
def yesNo(value): return 'YES' if value == 1 else 'NO'
 
def solve():
    k = it()
    each = defaultdict(list)
    for i in range(k):
        n = it()
        arr = li()
        sm = sum(arr)
        for j in range(n):
            if (arr[j],i + 1) not in each:
                each[(arr[j],i + 1)].append([i + 1, sm - arr[j] , j + 1])
    vals = [val[0] for val in each.values()]

    vals.sort(key=lambda x : x[1])
    ans = []
    for i in range(1, len(vals)):
        if vals[i][1] == vals[i - 1][1]:
            if vals[i - 1][0] != vals[i][0]:
                ans.append((vals[i][0], vals[i][2]))
                ans.append((vals[i - 1][0], vals[i - 1][2]))
                break
    
    if len(ans) < 2:
        print('NO')
    else:
        print('YES')
        for x , y in ans:
            print(x , y)
    # print(each)

    
 
t = 1
for _ in range(t):
    solve()