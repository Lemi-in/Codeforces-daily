n, m, k = map(int, input().split())
a = list(map(int, input().split()))

op = []
for _ in range(m):
    l, r, d = map(int, input().split())
    op.append((l, r, d))

q = []
for _ in range(k):
    x, y = map(int, input().split())
    q.append((x, y))

cnt = [0] * (m + 2)
for x, y in q:
    cnt[x] += 1
    cnt[y + 1] -= 1

for i in range(1, m + 1):
    cnt[i] += cnt[i - 1]

diff = [0] * (n + 2)
for i in range(m):
    l, r, d = op[i]
    diff[l] += d * cnt[i + 1]
    diff[r + 1] -= d * cnt[i + 1]

for i in range(1, n + 1):
    diff[i] += diff[i - 1]
    a[i - 1] += diff[i]

print(" ".join(map(str, a)))
