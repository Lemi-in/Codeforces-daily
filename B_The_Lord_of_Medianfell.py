
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

def check(mid, n, s):
    return ((n // 2) + 1) * mid <= s
def binary_search(n, s):
    l, r = 0, s
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        if check(mid, n, s):
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans
def solve():
    n, s = ints()
    ans = binary_search(n, s)
    print(ans)
 

     
   


t = it()
for _ in range(t):
    solve()

# You are given two positive integers n
#  and s
# . Find the maximum possible median of an array of n
#  non-negative integers (not necessarily distinct), such that the sum of its elements is equal to s
# .

# A median of an array of integers of length m
#  is the number standing on the ⌈m2⌉
# -th (rounding up) position in the non-decreasing ordering of its elements. Positions are numbered starting from 1
# . For example, a median of the array [20,40,20,50,50,30]
#  is the ⌈m2⌉
# -th element of [20,20,30,40,50,50]
# , so it is 30
# . There exist other definitions of the median, but in this problem we use the described definition.

# Input
# The input consists of multiple test cases. The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases. Description of the test cases follows.

# Each test case contains a single line with two integers n
#  and s
#  (1≤n,s≤109
# ) — the length of the array and the required sum of the elements.

# Output
# For each test case print a single integer — the maximum possible median.

# Example
# InputCopy
# 8
# 1 5
# 2 5
# 3 5
# 2 1
# 7 17
# 4 14
# 1 1000000000
# 1000000000 1
# OutputCopy
# 5
# 2
# 2
# 0
# 4
# 4
# 1000000000
# 0
# Note
# Possible arrays for the first three test cases (in each array the median is underlined):

# In the first test case [5–]
# In the second test case [2–,3]
# In the third test case [1,2–,2]
