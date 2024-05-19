
n = int(input())
b = list(map(int, input().split()))


a = [0] * n
maxx = 0


for i in range(n):
    a[i] = b[i] + maxx
    maxx = max(maxx, a[i])

print(*a)

