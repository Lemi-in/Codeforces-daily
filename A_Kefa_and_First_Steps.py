n = int(input())
a = list(map(int, input().split()))

left, right = 0 , 1
wind = 1
while right < n:
    if a[right] >= a [right - 1]:
        wind = max(wind, right - left + 1)
    else:
        left = right 
    right += 1
print(wind)