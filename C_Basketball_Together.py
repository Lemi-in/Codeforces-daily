n , d = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
l , r = 0 , n-1

cnt = 0
sm = 0
t = 0
for p in arr:
    diff = 1
    while diff > 0:
        diff += d - p
        cnt += 1
print(cnt)
    

