INF = 10**18
MAXN = 1000 + 25
ways = [0] * MAXN

def rem(x):
    for i in range(x, MAXN):
        ways[i] -= ways[i - x]

def add(x):
    for i in range(MAXN - 1, x - 1, -1):
        ways[i] += ways[i - x]

def solve():
    n, K = map(int, input().split())
    ar = list(map(int, input().split()))
    
    ways[0] = 1
    l = 0
    ans = INF
    
    for r in range(n):
        add(ar[r])
        while ways[K] != 0:
            ans = min(ans, r - l + 1)
            rem(ar[l])
            l += 1
    
    if ans > n:
        ans = -1
    print(ans)

# Call solve directly
t = 1  # Change this if you need multiple test cases
for _ in range(t):
    solve()
