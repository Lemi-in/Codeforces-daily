#author: Lemi
import sys

def solve():
    k = int(sys.stdin.readline().strip()) - 1  # Convert to 0-based index

    start, digit, cnt = 1, 1, 9

    while k >= digit * cnt:
        k -= digit * cnt
        start *= 10
        digit += 1
        cnt *= 10

    x, y = divmod(k, digit)  # Equivalent to k / digit and k % digit
    print(str(start + x)[y])  # Convert number to string and index

solve()
