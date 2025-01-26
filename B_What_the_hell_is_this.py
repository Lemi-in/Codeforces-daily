t = int(input())
for _ in range(t):
    d = int(input())
    nums = []
    seen = {}

    for i in range(d):
        n = int(input())
        arr = list(map(int, input().split()))
        for x in arr:
            seen[x] = i
        nums.append(arr)

    res = [-1] * d
    for i in range(d):
        for x in nums[i]:
            if seen[x] == i:
                res[i] = x
                break

    print(-1 if -1 in res else " ".join(map(str, res)))
