n, A, B = map(int, input().split())
sizes = list(map(int, input().split()))
sizes.sort(reverse=True)

total = sum(sizes)
curr = 0
hole = 0

for i in range(n):
    curr += sizes[i]
    hole += 1
    if curr * A >= B * total:
        break

print(hole - 1)
