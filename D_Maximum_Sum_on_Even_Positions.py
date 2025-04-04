#author: Lemi
import sys

def solve():
    n = it()
    arr = li()
    
    ans = sum(arr[i] for i in range(n) if i % 2 == 0)
    
    t1, mx = 0, 0
    for i in range(1, n, 2):
        t1 = max(0, arr[i] - arr[i - 1] + t1)
        mx = max(mx, t1)
    
    t1 = 0
    for i in range(2, n, 2):
        t1 = max(0, arr[i - 1] - arr[i] + t1)
        mx = max(mx, t1)

    print(ans + mx)

t = it()
for _ in range(t):
    solve()
