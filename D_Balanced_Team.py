n = int(input())
a = list(map(int, input().split()))

a.sort()
i, j = 0, 0
mx = 0

while j < n:
    if a[j] - a[i] <= 5:
        j += 1
    else:
        i += 1
    mx = max(mx, j - i)
print(mx)
