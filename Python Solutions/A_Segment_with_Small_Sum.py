n, s = map(int, input().split())
a = list(map(int, input().split()))

left, right = 0, 0
count = 0
miniSum = 0
while right < n:
    miniSum += a[right]
    while miniSum > s:
        miniSum -= a[left]
        left += 1
    right += 1
    count = max(count, right - left)

print(count)

    

