t = int(input())

for _ in range(t):
    n = int(input())
    shoes = list(map(int, input().split()))

    ans = []
    for i in range(1, n + 1):
        ans.append(i)

    l = 0
    r = 0
    permut = True
    while r < n:
        while r < n - 1 and shoes[r] == shoes[r + 1]: 
            r += 1
        if l == r:
            permut = False
        else:
            temp = ans[l+1:r+1]  
            temp.append(ans[l])  
            ans[l:r+1] = temp  
        l = r + 1
        r += 1
    if permut:
        print(*ans)
    else:
        print(-1)
