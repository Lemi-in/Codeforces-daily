n, k = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 10**9
result = -1

while left <= right:
    mid = left + (right - left) // 2
    count = 0
    
    for num in nums:
        if num <= mid:
            count += 1
    
    if count == k:
        result = mid
        break
    elif count < k:
        left = mid + 1
    else:
        right = mid - 1

print(result)
