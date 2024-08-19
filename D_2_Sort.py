for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [a[i] < 2 * a[i + 1] for i in range(n - 1)]
    sm = sum(b[:k])
    ans = 1 if sm == k else 0
    for i in range(k, n - 1):
        sm += b[i] - b[i - k]
        if sm == k:
            ans += 1
    print(ans)