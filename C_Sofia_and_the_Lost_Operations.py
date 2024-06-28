
t = int(input())
for _ in range(t):
    n = int(input())
    original = list(map(int, input().split()))
    target = list(map(int, input().split()))
    m = int(input())
    d = list(map(int, input().split()))
    c = [0] * m
    for i in range(m):
        c[i] = i
    n = len(original)
    
    for i in range(m):
        if i == n:
            #Now we go in certain order
            for j in range(i+1,n):
                original[j] = d[j]
            break
        original[i]  = d[i]
    print(original)
