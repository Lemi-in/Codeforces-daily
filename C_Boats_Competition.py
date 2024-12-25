for _ in range(int(input())):
    n = int(input())
    mp = [0] * (n + 1)
    w = list(map(int, input().split()))
    for x in w:
        mp[x] += 1

    mx = 0
    for sm in range(2, 2 * n + 1):
        currSum = 0
        for i in range(1, (sm + 1) // 2):
            if sm - i > n:
                continue
            currSum += min(mp[i], mp[sm - i])
        if sm % 2 == 0:
            currSum += mp[sm // 2] // 2
        mx = max(mx, currSum)
    
    print(mx)
