n, p = map(int, input().split())
arr = list(map(int, input().split()))

total = sum(arr)
arr = arr + arr
mn = float('inf') 
sm, l = 0, 0 
idx = -1

for r in range(2 * n):
    sm += arr[r]
    while sm >= p:
        if r - l + 1 < mn:
            mn = r - l + 1
            idx = l % n 
        sm -= arr[l]
        l += 1

if idx != -1:
    print(idx + 1, mn)
else:
    need = (p // total) * n
    al = total * (p // total)
    cnt = 0
    if al < p:
        pre = [0] * n
        pre[0] = arr[0]
        for i in range(1, n):
            pre[i] = pre[i - 1] + arr[i]
        for i in range(n):
            if al + pre[i] >= p:
                cnt = i + 1
                break
        print(1, need + cnt)
    else:
        print(1 , need)

# Read input
n, p = map(int, input().split())
v = list(map(int, input().split()))

total = sum(v)
ans = (p - v[0]) // total * n + 1
sum_val = (p - v[0]) // total * total + v[0]
l = pos = 0

if sum_val >= p:
    l = pos = 0
else:
    for i in range(n - 1, -1, -1):
        sum_val += v[i]
        ans += 1
        if sum_val >= p:
            pos = l = i
            break

length = ans
for r in range(1, n):
    sum_val += v[r]
    length += 1
    while sum_val >= p:
        sum_val -= v[l]
        l = (l + 1) % n
        length -= 1
    if length + 1 < ans:
        pos = (l - 1 + n) % n
        ans = length + 1

print(pos + 1, ans)
