n,m = map(int, input().split())
arr = []
sm = 0
for i in range(n):
    x,y = map(int, input().split())
    arr.append((x-y))
    sm += x
arr.sort(reverse=True)
for i in range(len(arr)):
    if sm <= m:
        print(i)
        exit()
    sm -= arr[i]
if sm <= m:
    print(n)
else:
    print(-1)