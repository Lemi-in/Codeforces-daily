#author: Lemi
import sys

def it(): return int(sys.stdin.readline())
def li(): return list(map(int, sys.stdin.readline().split()))

def solve():
    n = it()
    a = [0] + li()
    b = [0] + li()
    
    val = [False] * (n + 1)
    
    for _ in range(2):
        prvb = [0] * (n + 1)  # Previous smaller
        nxta = [0] * (n + 1)  # Next greater

        # Compute next greater element for `a`
        stack = [(10**9, n + 1)]
        for i in range(n, 0, -1):
            while stack[-1][0] <= a[i]:
                stack.pop()
            nxta[i] = stack[-1][1]
            stack.append((a[i], i))

        # Compute previous smaller element for `b`
        stack = [(0, 0)]
        for i in range(1, n + 1):
            while stack[-1][0] >= b[i]:
                stack.pop()
            prvb[i] = stack[-1][1]
            stack.append((b[i], i))

        # Checking conditions
        m = [0] * (n + 1)
        for i in range(1, n + 1):
            m[a[i]] = i
            if a[i] <= b[i] and m[b[i]]:
                val[i] |= prvb[i] < m[b[i]] and nxta[m[b[i]]] > i

        # Reverse the arrays for the second iteration
        a[1:], b[1:], val[1:] = a[1:][::-1], b[1:][::-1], val[1:][::-1]

    print("YES" if all(val[1:]) else "NO")

t = it()
for _ in range(t):
    solve()
