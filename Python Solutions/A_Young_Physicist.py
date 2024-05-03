n = int(input())
sumX = 0
sumY = 0
sumZ = 0\


for _ in range(n):
    a = list(map(int, input().split()))
    sumX += a[0]
    sumY += a[1]
    sumZ += a[2]

if sumX == 0 and sumY == 0 and sumZ == 0:
    print("YES")
else:
    print("NO")
