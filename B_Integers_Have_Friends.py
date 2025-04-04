t = II()
for _ in range(t):
    n = II()
    nums = LII()
    diffs = [abs(nums[i] - nums[i+1]) for i in range(n-1)]
    
    ans = 0
    tmp = [[-1, 1]]
    for i, v in enumerate(diffs):
        k = len(tmp)
        
        curr = v
        tmp.append([i, v])
        for idx in range(k-1, -1, -1):
            curr = math.gcd(curr, tmp[idx][1])
            tmp[idx][1] = curr
        
        new_tmp = [[-1, 1]]
        for idx, val in tmp:
            if val > new_tmp[-1][1]: new_tmp.append([idx, val])
            else: new_tmp[-1][0] = idx
        tmp = new_tmp
        ans = max(ans, i - tmp[0][0])
    
    print(ans + 1)