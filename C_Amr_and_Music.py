n, days = map(int, input().split())
arr = list(map(int, input().split()))
lst = []

for i in range(n):
    d = arr[i]
    lst.append((d, i))

lst.sort()

result = []

for i in range(n):
    if days < lst[i][0]:
        break
    result.append(lst[i][1] + 1)
    days -= lst[i][0]

result.sort()

print(len(result))
print(*result)

