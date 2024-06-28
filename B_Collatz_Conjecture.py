for _ in range(int(input())):
    x, y, k = map(int, input().split())
        
    limit = y - x % y
    if k < limit:
        result = x + k
    elif k == limit:
        x += k
        while x % y == 0:
            x //= y
            result = x
    elif k > limit:
        while True:
            if x == 1:
                break
            if k >= limit:
                k -= limit
                x += limit
                while x % y == 0:
                    x //= y
                limit = y - x % y
            elif k < limit:
                x += k
                k = 0
                break
        if k != 0:
            result = k % (y - 1) + 1
        else:
            result = x
        
    print(result)
