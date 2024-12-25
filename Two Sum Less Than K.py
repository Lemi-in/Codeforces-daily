def find(nums, k):
    nums.sort()
    mx = -1
    l , r = 0 , len(nums) - 1
    while l < r:
        sm = nums[l] + nums[r]
        if sm < k:
            mx = max(mx , sm)
            l += 1
        else:
            r -= 1
    return mx

nums = [10,20,30]
k = 15

print(find(nums, k))

