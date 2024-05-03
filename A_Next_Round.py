n, k = map(int, input().split())
a = list(map(int, input().split()))

if k == n and a[k - 1] > 0:
    print(k)
    exit()

if sum(a) == 0:
    print(0)
    exit()
    
if a[k - 1] == 0:
    for i in range(k - 1, -1, -1):
        if a[i] > 0:
            print(i + 1)
            exit()

winners = 0

for i in range(n):
    if a[i] >= a[k - 1]:
        winners += 1
print(winners)