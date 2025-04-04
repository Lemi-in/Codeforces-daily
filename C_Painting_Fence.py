# author: Lemi

import sys

def calc(a, l, r, mn):
    if l == r:
        return 0
    min_ = min(a[l:r])
    L = r - l
    cur = min_ - mn
    left = l

    for i in range(l, r):
        if a[i] == min_:
            cur += calc(a, left, i, min_)
            left = i + 1
        if cur > L:
            break

    if cur < L:
        cur += calc(a, left, r, min_)
    
    return min(L, cur)

def solve():
    N = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().split()))
    print(calc(a, 0, N, 0))

def main():
    sys.stdin = open(0)
    sys.stdout = open(1, "w")
    
    tt = 1
    # tt = int(input())  # Uncomment if multiple test cases are needed
    
    for _ in range(tt):
        solve()

if __name__ == "__main__":
    main()
