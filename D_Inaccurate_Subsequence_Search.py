t = int(input())

while t > 0:
    t -= 1
    n, m, k = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    cnt = {}
    for i in range(m):
        cnt[b[i]] = cnt.get(b[i], 0) + 1

    ans = 0
    good = 0

    for i in range(m - 1):
        good += cnt.get(a[i], 0) > 0
        cnt[a[i]] = cnt.get(a[i], 0) - 1

    for i in range(n - m + 1):
        good += cnt.get(a[i + m - 1], 0) > 0
        cnt[a[i + m - 1]] = cnt.get(a[i + m - 1], 0) - 1

        ans += (good >= k)

        cnt[a[i]] = cnt.get(a[i], 0) + 1
        good -= cnt[a[i]] > 0

    print(ans)
