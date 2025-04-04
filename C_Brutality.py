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
    n, k = ints()
    nums = li()
    string = s()

    ans = 0

    l = 0
    r = 0

    while l < len(nums):
        while r < len(nums):
            
            if string[l] != string[r]:
                break
            else:
                r += 1
        
        length = r - l + 1
        if length > k:
            ans += sum((sorted(nums[l:r])[::-1])[:k])
        else:
            ans += sum(nums[l:r])
        
        l = r

    print(ans)

    
 
t = 1
for _ in range(t):
    solve()

