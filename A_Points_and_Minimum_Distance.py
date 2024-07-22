
t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    for _ in range(2 * n):
        x = int(input())
        a.append(x)
    
    a.sort()
    pts = []
    for i in range(n):
        pts.append((a[i], a[i + n]))
    
    ans = 0
    for i in range(1, n):
        ans += abs(pts[i][0] - pts[i - 1][0]) + abs(pts[i][1] - pts[i - 1][1])
    
    print(ans)
    for pt in pts:
        print(pt[0], pt[1])
