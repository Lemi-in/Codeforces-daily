n = int(input())
arr = []
for _ in range(n):
    arr.append(input() )
temp = arr.copy()
arr.sort(key=len)

for i in range(n - 1):
    if arr[i] not in arr[i + 1]:
        print('NO')
        exit()
print('YES')
for i in range(n):
    print(arr[i])

