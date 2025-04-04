#author: Lemi
import sys
from bisect import bisect_left, bisect_right

def ls(): return sys.stdin.readline().split()
def ints(): return map(int, sys.stdin.readline().split())
def it(): return int(sys.stdin.readline())
def li(): return list(map(int, sys.stdin.readline().split()))

N = 2 * 10**5 + 5

def solve():
    n, t = ints()
    a = li()

    p = [0] * (n + 1)
    v = []
    fen = [0] * (N + 1)  # Fenwick Tree
    
    for i in range(1, n + 1):
        p[i] = p[i - 1] + a[i - 1]
        v.append(p[i])

    v.append(0)
    v = sorted(set(v))

    def add(x):
        while x < N:
            fen[x] += 1
            x += x & -x

    def get(x):
        r = 0
        while x > 0:
            r += fen[x]
            x -= x & -x
        return r

    def get_range(l, r):
        return get(r) - get(l - 1)

    ans = 0
    add(bisect_left(v, 0) + 1)

    for i in range(1, n + 1):
        id_ = bisect_left(v, p[i])
        jd = bisect_right(v, p[i] - t)
        ans += get_range(jd + 1, N - 1)
        add(id_ + 1)

    print(ans)

solve()
