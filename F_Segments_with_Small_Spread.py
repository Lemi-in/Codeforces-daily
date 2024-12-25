from collections import deque

def find_subarray_count(n, k, arr):
    mn = deque()
    mx = deque()
    ans = 0
    l = 0

    for i in range(n):
        while mn and arr[mn[-1]] > arr[i]:
            mn.pop()
        while mx and arr[mx[-1]] < arr[i]:
            mx.pop()
        mn.append(i)
        mx.append(i)

        while arr[mx[0]] - arr[mn[0]] > k:
            l += 1
            if mx[0] < l:
                mx.popleft()
            if mn[0] < l:
                mn.popleft()

        ans += (i - l + 1)

    return ans

n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(find_subarray_count(n, k, arr))
