t = int(input().strip())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().strip().split()))
    
    left = 0
    right = n - 1
    sShips = 0
    
    while k > 0 and left <= right:
        if k % 2 == 1:
            a[left] -= 1
            if a[left] == 0:
                left += 1
                sShips += 1
        else:
            a[right] -= 1
            if a[right] == 0:
                right -= 1
                sShips += 1
        k -= 1
    
    print(sShips)