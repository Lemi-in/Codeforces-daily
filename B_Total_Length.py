n  , s = map(int, input().split())
a = list(map(int, input().split()))

l = 0
sm = 0
cnt = 0
for r in range(n):
    sm += a[r]
    while sm > s:
        sm -= a[l]
        l += 1
    f = (r - l + 1) 
    cnt += (f * (f + 1)) // 2
print(cnt)

# 2 6 4 3 6 8 9  
# 2 6 4 3 6 8    
# 2 6 4 3 6      
# 2 6 4 3  4
# 2 6 4    3
# 2 6      2
# 2        1
# 1
# 2
# 10
# 10
# 6
# 2
# 6 4 3 6 8 9
# 6 4 3 6 8
# 6 4 3 6
# 6 4 3
# 6 4
# 6 

# 4 3 6 8 9
# 4 3 6 8
# 4 3 6
# 4 3
# 4

# 3 6 8 9
# 3 6 8
# 3 6
# 3

# 6 8 9
# 6 8
# 6

# 8 9
# 8

# 9



