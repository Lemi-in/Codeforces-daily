n , s = map(int, input().split())
w = list(map(int, input().split()))
c = list(map(int, input().split()))

l  = 0 
curSm = 0
curCst = 0
mx = 0
for r in range(n):
    curSm += w[r]
    curCst += c[r]
    while curSm > s:
        curSm -= w[l]
        curCst -= c[l]
        l += 1
    mx = max(mx , curCst)
print(mx)

