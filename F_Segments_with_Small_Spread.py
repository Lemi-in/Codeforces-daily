# Template Author: Lemi
import sys
import heapq
import math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
from math import ceil, sqrt, gcd

def ls(): return sys.stdin.readline().split()
def ints(): return map(int, sys.stdin.readline().split())
def strs(): return map(str, sys.stdin.readline().split())
def it(): return int(sys.stdin.readline())
def s(): return sys.stdin.readline().strip()
def li(): return list(map(int, sys.stdin.readline().split()))
 
def solve():
    
    n , k = ints()
    arr = li()

    max_heap = []
    min_heap = []

    removed = defaultdict(int)

    l = 0
    segments = 0
    for r in range(n):
        heapq.heappush(min_heap, arr[r])
        heapq.heappush(max_heap, -arr[r])

        while -max_heap[0] - min_heap[0] > k:
            removed[arr[l]] += 1
            l += 1

            while max_heap and removed[-max_heap[0]] > 0:
                removed[-max_heap[0]] -= 1
                heapq.heappop(max_heap)

            while min_heap and removed[min_heap[0]] > 0:
                removed[min_heap[0]] -= 1
                heapq.heappop(min_heap)
        segments += ( r - l + 1)

    print(segments)
 
 
t = 1
for _ in range(t):
    solve()