for _ in range(int(input())):  
    n ,l,r  = map(int, input().split())
    arr = list(map(int, input().split()))  
    win ,sm = 0 , 0
    i = 0

    for j in range(n):
        sm += arr[j]
        while sm > r and i <= j:
            sm -= arr[i]
            i += 1
        if l <= sm and sm <= r:
            win += 1
            sm = 0
            i = j + 1

    print(win)  
