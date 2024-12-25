def minSwaps(arr):
    k = arr.count(1)
    l, r, cnt, mx = 0, 0, 0, 0
    
    while r < len(arr):
        cnt += arr[r]
        if r - l + 1 > k:
            cnt -= arr[l]
            l += 1
        if r - l + 1 == k:
            mx = max(mx, cnt)
        r += 1
    
    return k - mx

arr = [1,0,1,0,1]
print(minSwaps(arr)) 
