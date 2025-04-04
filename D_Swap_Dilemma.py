def count_inversions(arr, l, r):
    if l == r:
        return 0
    
    mid = (l + r) // 2
    x = count_inversions(arr, l, mid)
    y = count_inversions(arr, mid + 1, r)
    
    # Merging process
    temp = []
    inv = 0
    left, right = l, mid + 1
    
    while left <= mid and right <= r:
        if arr[left] < arr[right]:
            inv += right - mid - 1
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        inv += right - mid - 1
        temp.append(arr[left])
        left += 1

    while right <= r:
        temp.append(arr[right])
        right += 1

    # Copy merged elements back to the original array
    arr[l:r+1] = temp

    return x + y + inv


def solve():
    n = int(input().strip())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    x = sorted(a)
    y = sorted(b)

    if x != y:
        print("NO")
        return
    
    print("YES" if count_inversions(a, 0, n - 1) % 2 == count_inversions(b, 0, n - 1) % 2 else "NO")


t = int(input().strip())
for _ in range(t):
    solve()
