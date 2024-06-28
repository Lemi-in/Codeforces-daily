n, t = map(int, input().split())
a = list(map(int, input().split()))

start = 0
currSum = 0
maxSum= 0

for end in range(n):
    currSum += a[end]
    while currSum > t:
        currSum -= a[start]
        start += 1
    maxSum= max(maxSum , end - start + 1)

print(maxSum)
