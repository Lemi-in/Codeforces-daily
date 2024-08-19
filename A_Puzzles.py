n, m = map(int, input().split())
p = list(map(int, input().split()))
p.sort()

diff = float('inf')
for i in range(m - n + 1):
    diff = min(diff, p[i + n - 1] - p[i])

print(diff)