import sys
import bisect

def rec(l, r):
    i = bisect.bisect_left(avengers, l)
    j = bisect.bisect_right(avengers, r) - 1

    x = j - i + 1  # Number of avengers in the range
    if x == 0:
        power_consumed = A
    else:
        power_consumed = B * x * (r - l + 1)  # Power consumed for operation 2

    if l == r or x == 0:
        return power_consumed

    mid = (l + r) // 2
    return min(power_consumed, rec(l, mid) + rec(mid + 1, r))

if __name__ == "__main__":
    sys.stdin = open(0)  # Fast input reading
    n, k, A, B = map(int, sys.stdin.readline().split())
    
    avengers = list(map(int, sys.stdin.readline().split()))
    avengers.sort()

    x = 1 << n  # Equivalent to 2^n
    print(rec(1, x))
