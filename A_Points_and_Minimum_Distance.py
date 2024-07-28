t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    m = n * 2
    pts = []
    l , r = 0 , m - 1
    while l < r:
        pts.append((a[l],a[r]))
        l += 1
        r -= 1
    sm = 0
    for i in range(len(pts) - 1):
        sm += abs(pts[i][0] - pts[i + 1][0])
        sm += abs(pts[i][1] - pts[i + 1][1])
    print(sm)
    for x , y in pts:
        print( x , y)

