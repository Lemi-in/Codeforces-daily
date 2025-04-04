#author: Lemi
import sys

def solve():
    n, k = map(int, sys.stdin.readline().split())
    k -= 1  # Decrease k to match 0-based index behavior in C++

    ans = [0] * n
    l, r = 0, n - 1

    for i in range(1, n):
        if (k >> (n - i - 1)) & 1:
            ans[r] = i
            r -= 1
        else:
            ans[l] = i
            l += 1

    ans[l] = n  # The last element is always 'n'
    print(*ans)

solve()
