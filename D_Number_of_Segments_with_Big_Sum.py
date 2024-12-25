n, s = map(int, input().split())
a = list(map(int, input().split()))
 
l, r = 0, 0
cnt = 0
sm = 0
while r < n:
    sm += a[r]
    while sm >= s:
        cnt += n - r
        sm -= a[l]
        l += 1
    
    r += 1
 
print(cnt)

