cal = [3,2]
n = len(cal)
k = 2
lower = 0
upper = 1
l = 0
T = 0
sm = 0
for r in range(n):
    sm += cal[r]
    if r - l + 1 > k:
        sm -= cal[l]
        l += 1
    if r - l + 1 == k:
        if sm < lower:
            T -= 1
        elif sm > upper:
            T += 1
    
print(T)