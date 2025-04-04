

q = int(input())
while q:
    q -= 1
    n, k = map(int, input().split())

    a = [int(2e9)] * (n + 3)
    pos = list(map(int, input().split()))
    temp_values = list(map(int, input().split()))

    for i in range(k):
        a[pos[i]] = temp_values[i]

    for i in range(1, n + 1):
        if a[i - 1] + 1 < a[i]:
            a[i] = a[i - 1] + 1

    for i in range(n, 0, -1):
        if a[i + 1] + 1 < a[i]:
            a[i] = a[i + 1] + 1

    for i in range(1, n + 1):
        print(a[i], end=' ')
    print()
