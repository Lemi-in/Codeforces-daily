n , m = map(int, input().split())
arr = []
for i in range(m):
    a , b = map(int, input().split())
    arr.append((a,b))

arr.sort(key=lambda x: x[1], reverse=True)
ans = 0
for c , y in arr:
    if n > 0:
        ans += (y * min(n, c))
        n -= min(n, c)
        
print(ans)

