#author: Lemi
import sys

def it(): return int(sys.stdin.readline())
def li(): return list(map(int, sys.stdin.readline().split()))

def canMeetInTime(m, x, v):
    min_pos = float('-inf')
    max_pos = float('inf')

    for i in range(len(x)):
        left = x[i] - ( m * v[i])  
        right = x[i] + ( m * v[i])
        
        min_pos = max(min_pos, left)
        max_pos = min(max_pos, right)
    
    return min_pos <= max_pos  
def solve():
    n = it()
    x = li()
    v = li()

    l, r = 0, max(x)
    while r - l >= 1e-6:
        mid = (l + r) / 2
        if canMeetInTime(mid, x, v):
            r = mid
        else:
            l = mid

    print(r)

t = 1
for _ in range(t):
    solve()
