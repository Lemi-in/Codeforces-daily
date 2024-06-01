for _ in range(int(input().strip())):
    num11, numtt = map(int, input().split())
    
    if numtt % 2 == 0:
        first = numtt // 2
    else:
        first = (numtt // 2) + 1

    if numtt % 2 == 0:
        maxx = 7 * (numtt // 2)
    else:
        maxx = (7 * (numtt // 2)) + 11
    
    num11 -= maxx
    
    if num11 <= 0:
        print(first)
    else:
        screen = first
        while num11 > 0:
            screen += 1
            num11 -= 15
        print(screen)
