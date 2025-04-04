n = int(input())
arr = list(map(int, input().split()))

arr.sort()
first = []
last = []

for i in range(n):
    if i < n // 2:
        first.append(arr[i])
    else:
        last.append(arr[i])

final = []
jj = 0
ii = 0

for i in range(n):
    if i % 2 == 0:
        final.append(last[jj])
        jj += 1
    else:
        final.append(first[ii])
        ii += 1

ctr = 0
for i in range(1, n - 1):
    if final[i] < final[i - 1] and final[i] < final[i + 1]:
        ctr += 1

print(ctr)
print(*final)
