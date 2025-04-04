import sys
import math

LOGN = 20
stGCD = []

def get_gcd(l, r):
    k = (r - l + 1).bit_length() - 1
    return math.gcd(stGCD[k][l], stGCD[k][r - (1 << k) + 1])

def solve():
    global stGCD
    stGCD = []
    
    n, q = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))

    b = [abs(a[i - 1] - a[i]) for i in range(1, n)]

    stGCD = [[1] * len(b) for _ in range(LOGN)]
    for i in range(len(b)):
        stGCD[0][i] = b[i]

    for i in range(1, LOGN):
        for j in range(len(b) - (1 << (i - 1))):
            stGCD[i][j] = math.gcd(stGCD[i - 1][j], stGCD[i - 1][j + (1 << (i - 1))])

    output = []
    for _ in range(q):
        l, r = map(int, sys.stdin.readline().split())
        if l == r:
            output.append("0")
        else:
            l -= 1
            r -= 2
            output.append(str(get_gcd(l, r)))

    print(" ".join(output))

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        solve()
        print()
