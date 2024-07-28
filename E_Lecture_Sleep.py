n, k = map(int, input().split())
a = list(map(int, input().split()))
t = list(map(int, input().split()))

res = 0
for i in range(n):
    if t[i] == 1:
        res += a[i]
        a[i] = 0

prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + a[i]

max_theorems = res
for i in range(n - k + 1):
    max_theorems = max(max_theorems, res + prefix_sum[i + k] - prefix_sum[i])

print(max_theorems)