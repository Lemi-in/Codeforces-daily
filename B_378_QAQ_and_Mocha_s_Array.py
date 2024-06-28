t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    if 1 in a:
        print("Yes")
        continue

    a.sort()
    b = [x for x in a if x % a[0] != 0]
    
    if not b:
        print("Yes")
        continue
    
    c = [x for x in b if x % b[0] != 0]
    
    if not c:
        print("Yes")
    else:
        print("No")
