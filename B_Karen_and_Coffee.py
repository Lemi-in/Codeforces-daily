n, k, q = map(int, input().split())
rnge = []
mx = 200000
diff = [0] * (mx + 2)


for _ in range(n):
    l, r = map(int, input().split())
    diff[l] += 1
    diff[r + 1] -= 1
pref = [0] * (mx + 2)
for i in range(1, mx + 1):
    diff[i] += diff[i - 1]
    pref[i] = pref[i - 1] + (1 if diff[i] >= k else 0)

for _ in range(q):
    x, y = map(int, input().split())
    print(pref[y] - pref[x - 1])
