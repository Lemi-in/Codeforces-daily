t = int(input())
for _ in range(t):
    n = int(input())
    arr = 0
    ans = []
    for i in range(n):
        l, r = map(int, input().split())
        if arr >= r:
            ans.append(0)
        else:
            ans.append(max(arr + 1, l))
            arr = ans[-1]
    print(*ans)