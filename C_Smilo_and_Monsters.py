N = int(2e5) + 10
a = [0] * N

t = int(input())
while t:
    t -= 1
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(1, n + 1):
        a[i] = arr[i - 1]

    a[1:n + 1] = sorted(a[1:n + 1])

    ans = 0
    i = 1
    j = n
    x = 0

    while i <= j:
        if i == j:
            if a[j] == 1:
                ans += 1
                break
            ans += ((a[j] - x) + 1) // 2 + 1
            break
        
        if x + a[i] >= a[j]:
            ans += (a[j] - x) + 1
            a[i] -= (a[j] - x)
            x = 0
            j -= 1
            if a[i] == 0:
                i += 1
        else:
            ans += a[i]
            x += a[i]
            i += 1

    print(ans)
