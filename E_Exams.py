n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))
arr.sort()
days = -1
for a, b in arr:
    if days <= b:
        days = b
    else:
        days = a

print(days)