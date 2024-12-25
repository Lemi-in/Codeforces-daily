nums = [1,-1,5,-2,3]
k = 3

ans = s = 0
for i , x in enumerate(nums):
    s += x
    if s == k:
        ans = i + 1
    elif s - k in nums:
        ans = max(ans, i - nums.index(s - k))
print(ans)

#or we can use a dictionary to store the sum and the index

nums = [1,-1,5,-2,3]
k = 3
dic = {0:-1}

for i , x in enumerate(nums):
    s += x
    if s - k in dic:
        ans = max(ans, i - dic[s - k])
    if s not in dic:
        dic[s] = i
print(ans)

