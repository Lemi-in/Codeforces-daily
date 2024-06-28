for _ in range(int(input())):
    n, f, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    fav = a[f - 1]
    sorted_a = sorted(a, reverse=True)
    
    pas = [i for i, val in enumerate(sorted_a) if val == fav]
    
    if pas[0] < k:
        if pas[-1] < k:
            print("YES")
        else:
            print("MAYBE")
    else:
        print("NO")
