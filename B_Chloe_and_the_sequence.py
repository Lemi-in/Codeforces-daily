n, k = map(int, input().split())
size = 1
for _ in range(1, n):
    size = size * 2 + 1

left, right, target, ans = 1, size, k, n
while left <= right:
    mid = (left + (right - left) // 2)
    if target < mid:
        right = mid - 1
        ans -= 1
    elif target > mid:
        left = mid + 1
        ans -= 1
    else:
        break

print(ans)