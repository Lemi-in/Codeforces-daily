t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    i , j = 0, n - 1
    step = 0
    
    while i <= j:
        if arr[i] == 1 and arr[j] == 0:
            step += 1
            i += 1
            j -= 1
        elif arr[i] == 0 and arr[j] == 1:
            i += 1
            j -= 1
        elif arr[i] == 1 and arr[i] == 1:
            j -= 1
        else:
            i += 1
    print(step)