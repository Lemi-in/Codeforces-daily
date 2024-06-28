n = int(input())
for _ in range(n):
    a , b  = input().split()
    a , b = list(a) ,  list(b)
    temp = a[0]
    a[0] = b[0]
    b[0] = temp
    print("".join(a) , "".join(b))
    
