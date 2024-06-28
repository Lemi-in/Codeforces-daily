t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    mEven = 0
    mOdd = 0
    
    for i in range(n):
        if i % 2 != arr[i] % 2:
            if i % 2 == 0:
                mEven += 1
            else:
                mOdd += 1
    
    if mEven == mOdd:
        print(mEven)
    else:
        print(-1)
