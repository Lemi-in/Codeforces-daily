n, k = map(int, input().split())
nums = sorted(map(int, input().split()))
 
left, right = 1, 10**9
result = -1
 
while left <= right:
    mid = (left + right) // 2
    count = 0
    print("mid: ", mid)
    
    for num in nums:
        if num <= mid:
            count += 1
            print("count: ", count)
        
    if count == k:
        result = mid
        break
    elif count < k:
        left = mid + 1
    else:
        right = mid - 1
 
print(result)