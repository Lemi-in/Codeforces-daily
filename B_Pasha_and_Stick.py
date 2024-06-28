n = int(input().strip())

if n % 2 != 0:
    print(0)
else:
    h = n // 2
    
    if h % 2 == 0:
        print(h // 2 - 1)
    else:
        print(h // 2)
