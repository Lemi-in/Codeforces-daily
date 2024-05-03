n, s = map(int, input().split())
a = list(map(int, input().split()))

left, right = 0, 0
goodSegment = 0
maxSum = float('inf')
while right < n:
    goodSegment += a[right]
    while maxSum >= s:
        goodSegment = min(goodSegment , right - left + 1)
        maxSum -= a[left]
        left += 1
    right += 1
    
if maxSum == float('inf'):
    print(-1)
else:
    print(goodSegment)

    

