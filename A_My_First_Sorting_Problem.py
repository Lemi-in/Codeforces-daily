n = int(input())
for _ in range(n):
    a , b = map(int, input().split())
    if a > b:
        a, b = b, a
    print
    
