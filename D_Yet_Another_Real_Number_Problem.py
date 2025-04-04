#author: Lemi
import sys

def it(): return int(sys.stdin.readline())
def li(): return list(map(int, sys.stdin.readline().split()))

MOD = 1000000007

def countr_zero(x):
    return (x & -x).bit_length() - 1 if x else 0

def power(a, r):
    res = 1
    while r:
        if r & 1:
            res = res * a % MOD
        a = a * a % MOD
        r >>= 1
    return res

def solve():
    n = it()
    arr = li()

    stack = []
    sum_ = 0

    for ai in arr:
        r = countr_zero(ai)
        a = ai >> r

        while stack:
            if r >= 30 or stack[-1][0] <= (a << r):
                r += stack[-1][1]
                sum_ += stack[-1][0]
                stack.pop()
            else:
                break

        if r == 0:
            sum_ += a
        else:
            stack.append((a, r))

        res = sum_
        for a, r in stack:
            res = (res + power(2, r) * a) % MOD
        
        print(res, end=" ")
    
    print()

t = it()
for _ in range(t):
    solve()
