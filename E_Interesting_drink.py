n = int(input())
a = list(map(int, input().split()))
q = int(input())
arr = []
for _ in range(q):
    m = int(input())
    arr.append(m)
a.sort()
for num in arr:
    x, y = 0, n - 1
    ans = -1
    while x <= y:
        mid = (x + y) // 2
        if a[mid] <= num:
            ans = mid
            x = mid + 1
        else:
            y = mid - 1
    print(ans + 1)
