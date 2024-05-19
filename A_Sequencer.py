t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    l , r = 0 , n - 1
    ans = []
    while l <= r:
        if l == r:
            ans.append(a[l])
        else:
            ans.append(a[l])
            ans.append(a[r])
        l += 1
        r -= 1
    print(*ans)