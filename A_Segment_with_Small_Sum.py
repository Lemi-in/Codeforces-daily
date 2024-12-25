n , s = map(int, input().split())
arr = list(map(int, input().split()))

l , r  = 0 , 0
sm , mx = 0 , 0 

while r < n:
    sm += arr[r]
    while sm > s:
        sm -= arr[l]
        l += 1
    mx = max(mx , r - l + 1)
    r += 1
print(mx)
