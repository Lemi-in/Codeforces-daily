

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    table = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            table[j][(i+j)%n] = int(s[i])
    dp = [[0]*n for _ in range(n)]
    for j in range(n):
        count = 0
        for i in range(n):
            if table[i][j] == 1:
                count += 1
            else:
                count = 0
            dp[i][j] = count
    for i in range(n):
        count = 0
        for j in range(n):
            if table[i][j] == 1:
                count += 1
            else:
                count = 0
            dp[i][j] = min(dp[i][j], count)
    for j in range(1, n):
        for i in range(1, n):
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + dp[i][j])
    print(max(dp[i][j] for i in range(n) for j in range(n)))
