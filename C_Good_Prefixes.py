

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    sm = cnt = mx = i = 0
    while i < n :
        sm += arr[i]
        mx = max(mx, arr[i])
        if sm - mx == mx:
            cnt += 1
        i += 1
    print(cnt)