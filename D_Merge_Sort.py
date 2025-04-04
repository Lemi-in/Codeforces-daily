#author: Lemi
import sys

def op(l, r):
    global k, ans
    if k == 0 or l + 1 == r:
        return
    m = (l + r) // 2
    k -= 1
    ans[m - 1], ans[m] = ans[m], ans[m - 1]
    op(l, m)
    op(m, r)

def solve():
    global k, ans
    n, k = map(int, sys.stdin.readline().split())

    if k % 2 == 0:
        print(-1)
        return
    
    ans = list(range(1, n + 1))
    k //= 2
    op(0, n)

    if k:
        print(-1)
    else:
        print(*ans)

solve()
