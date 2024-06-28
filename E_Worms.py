n = int(input())
worms = list(map(int, input().split()))
m = int(input())
l = list(map(int, input().split()))

pf = [0] * (n + 1)
for i in range(1, n + 1):
    pf[i] = pf[i - 1] + worms[i - 1]

for q in l:
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if pf[mid] >= q:
            right = mid
        else:
            left = mid + 1
    print(left)
