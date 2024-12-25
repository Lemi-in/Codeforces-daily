n, m = map(int, input().split())
a = list(map(int, input().split()))
unique = [0] * n
seen = set()

for i in range(n - 1, -1, -1):
    seen.add(a[i])
    unique[i] = len(seen)

for _ in range(m):
    l = int(input())
    print(unique[l - 1])
