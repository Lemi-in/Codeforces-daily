#author: Lemi
import sys, heapq

def it(): return int(sys.stdin.readline())
def li(): return list(map(int, sys.stdin.readline().split()))

def solve():
    n = it()
    arr = li()
    
    l, r = 0, n - 1
    min_heap = [(arr[i], i) for i in range(n)]
    max_heap = [(-arr[i], i) for i in range(n)]
    
    heapq.heapify(min_heap)
    heapq.heapify(max_heap)

    valid = lambda x: l <= x <= r

    while l < r:
        while min_heap and not valid(min_heap[0][1]):
            heapq.heappop(min_heap)
        while max_heap and not valid(max_heap[0][1]):
            heapq.heappop(max_heap)
        
        mn, mx = min_heap[0][0], -max_heap[0][0]
        
        if arr[l] != mn and arr[r] != mn and arr[l] != mx and arr[r] != mx:
            print(l + 1, r + 1)
            return

        if arr[l] == mn or arr[l] == mx:
            l += 1
        elif arr[r] == mn or arr[r] == mx:
            r -= 1

    print(-1)

t = it()
for _ in range(t):
    solve()
