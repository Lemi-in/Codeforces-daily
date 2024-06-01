t = int(input().strip())
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    
    odd = [x for x in a if x % 2 == 1]
    even = [x for x in a if x % 2 == 0]
    a = odd + even
    
    print(*a)