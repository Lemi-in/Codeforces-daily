def binary_search(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    
    # Initialize count and indices lists
    count = [[0] * 10001 for _ in range(n + 1)]
    indices = [[] for _ in range(10001)]
    
    beautiful = 0
    
    # Build count and indices lists
    for i in range(n - 2):
        beautiful += len(indices[a[i + 1]]) - binary_search(indices[a[i + 1]], i + 2)
        indices[a[i]].append(i + 1)
        indices[a[i + 1]].append(i + 2)
        count[i + 1][a[i]] += 1
        count[i + 2][a[i + 1]] += 1
        count[i + 1][a[i + 1]] -= 1
        count[i + 2][a[i]] -= 1
    
    print(beautiful)
