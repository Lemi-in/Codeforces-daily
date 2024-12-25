t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    l , r = 0 , n - 1
    arr
    cnt = 0
    while l < r:
        arr.sort()
        mid = (l + r) // 2
        if arr[l] - arr[mid] >= arr[r]- arr[mid]:
            arr[l] = arr[mid]
            cnt += 1
        elif arr[l] - arr[mid] < arr[r] - arr[mid]:
            arr[r] = arr[mid]
            cnt += 1
        l += 1
        r -= 1
    print(cnt)
            
    