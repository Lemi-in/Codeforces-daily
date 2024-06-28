from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    freq = Counter(a)
    f = len(freq)
    ans = [0] * n
    for i in range(f):
        ans[i] = f
    for i in range(f, n):
        ans[i] = i + 1
    print(*ans)