t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    sm1 = abs(a[0] - a[0]) + abs(a[1] - a[0]) + abs(a[2] - a[0])
    sm2 = abs(a[0] - a[1]) + abs(a[1] - a[1]) + abs(a[2] - a[1])
    sm3 = abs(a[0] - a[2]) + abs(a[1] - a[2]) + abs(a[2] - a[2])
    print(min(sm1, sm2, sm3))
    
        