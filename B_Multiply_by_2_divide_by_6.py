t = int(input())
for _ in range(t):
    n = int(input())
    count2 , count3 = 0 , 0
    while n % 2 == 0:
        n = n // 2
        count2 += 1
    while n % 3 == 0:
        n = n // 3
        count3 += 1
    if n == 1 and count2 <= count3:
        print(2 * count3 - count2) 
    else:
        print(-1)