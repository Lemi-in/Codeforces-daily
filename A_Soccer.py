t = int(input())
for _ in range(t):
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    
    x = x1 - y1
    y = x2 - y2
    
    if x != 0 and y!= 0:
        if (x > 0 and y< 0) or (x < 0 and y> 0):
            print("NO")
        else:
            print("YES")
    else:
        print("NO")
