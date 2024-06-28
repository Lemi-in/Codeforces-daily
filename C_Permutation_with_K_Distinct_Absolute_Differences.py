n, k = map(int, input().split())

ans = []

curr = 1
prev = 0
i = 1

while i < k + 2:
    if i == 1:
        curr = 1
    else:
        if i % 2 == 0:
            curr = k + 2 - prev
        else:
            curr = k + 3 - prev
    ans.append(curr)
    prev = curr
    i += 1
i = k + 2
while i <= n:
    ans.append(i)
    i += 1

print(*ans)
