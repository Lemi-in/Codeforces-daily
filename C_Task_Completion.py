t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    time = 0
    ans = [0] * n
    for i in range(n):
        time = max(time, a[i])
        ans[i] = b[i] - time 
        time = b[i]

    print(*ans)