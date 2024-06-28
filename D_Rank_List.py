
n, k = map(int, input().split())
nums = []
for _ in range(n):
    c , b = map(int, input().split())
    nums.append((c, b))

nums.sort(key=lambda x: (-x[0], x[1]))

result = 0
penalty1, penalty2= nums[k-1]
for i in range(n):
    if nums[i] == (penalty1, penalty2):
        result += 1

print(result)