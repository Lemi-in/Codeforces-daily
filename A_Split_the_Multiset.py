t = int(input().strip()) 
for _ in range(t):
    n, k = map(int, input().strip().split())
    arr = [n]
    num = 0
    while len(arr) < n:
        curr = arr.pop()
        for i in range(min(k - 1, curr - 1)):
            arr.append(1)
        arr.append(curr - (k - 1))
        num += 1
    
    print(num)
