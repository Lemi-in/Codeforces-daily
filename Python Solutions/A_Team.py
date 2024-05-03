n = int(input())
count = 0

for _ in range(n):
    a = list(map(int, input().split()))
    summ = sum(a)
    if summ >= 2:
        count += 1
print(count)
