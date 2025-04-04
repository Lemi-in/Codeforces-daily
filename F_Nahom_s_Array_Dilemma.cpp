from collections import deque
from sys import stdin

def I(): return int(stdin.readline().strip())
def IL(): return list(map(int, stdin.readline().strip().split()))

def solve():
    n = I()
    a = IL()
    
    pre = [0] * n
    pre[0] = a[0]
    
    # Calculating the prefix sum manually
    for i in range(1, n):
        pre[i] = pre[i - 1] + a[i]

    q = deque()

    for i in range(n):
        while q and a[q[-1]] <= a[i]:
            idx = q.pop()
            temp = pre[i]
            if idx:
                temp -= pre[idx - 1]
            if temp > a[i]:
                print("NO")
                return
        q.append(i)

    q.clear()

    for i in range(n - 1, -1, -1):
        while q and a[q[-1]] <= a[i]:
            idx = q.pop()
            temp = pre[idx]
            if i:
                temp -= pre[i - 1]
            if temp > a[i]:
                print("NO")
                return
        q.append(i)

    print("YES")
    
T = I()
for _ in range(T):
    solve()
