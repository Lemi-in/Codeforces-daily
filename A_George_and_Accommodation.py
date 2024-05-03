n = int(input())
count = 0
for _ in range(n):
    p , q = map(int, input().split())
    diff = q - p
    if diff >= 2:
        count += 1
print(count)