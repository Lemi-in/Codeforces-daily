from collections import Counter

n, m = map(int, input().split())
a = list(map(int, input().split()))
fruits = [input() for _ in range(m)]

mp = sorted(Counter(fruits).values(), reverse=True)

a.sort()

mn, mx = 0, 0
for i, val in enumerate(mp):
    mn += val * a[i]

for i, val in enumerate(mp):
    mx += val * a[-(i + 1)]

print(mn, mx)
