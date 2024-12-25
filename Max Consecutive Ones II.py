nums = [1, 0, 1, 1, 0, 1]
l, r, sm, mx = 0, 0, 0, 0

while r < len(nums):
    sm += nums[r]
    if (r - l + 1) - sm > 1:
        sm -= nums[l]
        l += 1
    mx = max(mx, r - l + 1)
    r += 1

print(mx)
