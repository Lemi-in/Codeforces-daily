t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # Check if it is possible to make all the elements of the array equal to zero
    for i in range(1, n):
        if a[i] > a[i-1]:
            # It is not possible to make all the elements of the array equal to zero
            print("NO")
            break
    else:
        # It is possible to make all the elements of the array equal to zero
        print("YES")