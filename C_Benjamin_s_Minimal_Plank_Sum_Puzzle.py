n , k = map(int, input().split())
arr = list(map(int, input().split()))
i , j = 0 , 0
sm= float("inf")
f = -1
tmp = 0

while j < n:
    tmp += arr[j]
    if (j - i + 1) == k and tmp < sm:
        sm = tmp
        tmp -= arr[i]
        f = i + 1
        i += 1
    elif (j - i + 1) == k:
        tmp -= arr[i]
        i += 1
    j += 1
print(f)