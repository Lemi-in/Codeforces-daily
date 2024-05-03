n = int(input())
chemforces = {}
for _ in range(n):
    a, x = map(int, input().split())
    chemforces[a] = x

m = int(input())
topchemist = {}
for _ in range(m):
    b, y = map(int, input().split())
    topchemist[b] = y

total_income = 0

for a, x in chemforces.items():
    if a not in topchemist:
        total_income += x


for b, y in topchemist.items():
    if b not in chemforces:
        total_income += y
    elif b in chemforces:
        if chemforces[b] < y:
            total_income += y
        else:
            total_income += chemforces[b]

print(total_income)
