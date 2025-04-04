#author: Lemi
import sys

def merge(arr, temp, left, mid, right):
    i, j, k = left, mid, left
    count = 0

    while i <= mid - 1 and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
            count += (mid - i)
        k += 1

    while i <= mid - 1:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp[i]

    return count

def merge_sort(arr, temp, left, right):
    count = 0
    if right > left:
        mid = (left + right) // 2
        count += merge_sort(arr, temp, left, mid)
        count += merge_sort(arr, temp, mid + 1, right)
        count += merge(arr, temp, left, mid + 1, right)
    return count

def count_inversions(arr):
    temp = arr[:]
    return merge_sort(arr, temp, 0, len(arr) - 1)

def solve():
    n = it()
    arr = li()
    
    res = count_inversions(arr)
    arr.sort()

    curr = 1
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            res += (curr * (curr - 1)) // 2
            curr = 1
        else:
            curr += 1
    
    res += (curr * (curr - 1)) // 2
    print(res)

t = it()
for _ in range(t):
    solve()
