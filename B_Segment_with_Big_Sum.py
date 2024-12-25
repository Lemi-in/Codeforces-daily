n, s = map(int, input().split())
a = list(map(int, input().split()))
 
l, r = 0, 0
mn = float('inf')  
sm = 0
while r < n:
    sm += a[r]
    while sm >= s:
        mn = min(mn, r - l + 1)
        sm -= a[l]
        l += 1
    r += 1
 
if mn == float('inf'):
    print(-1)
else:
    print(mn)

