
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
    mod=1000000007
    n , k =  map(int,input().split())
    arr = list(map(int,input().split()))
    j=0
    # for i in range(n):
    #     arr[i]*=(1<<j)
    #     j+=1

    ans = 0
    k += 1
    temp = 1
    
    # print(arr)
    for i in range(1,n):
        if 2*arr[i]-(arr[i-1])>0:
            temp += 1
        else:
            temp = 1
        # print(temp)
        
        if temp == k:
            ans += 1
            temp -= 1
    print(ans)

 
 
t = it()
for _ in range(t):
    solve()