# Link: https://codeforces.com/contest/1475/problem/A


# Brute force solution time complexity is O(logn)
t = int(input())
for _ in range(t):
    n = int(input())
    while n % 2 == 0:
        n //= 2
    if n > 1:
        print("YES")
    else:
        print("NO")
        
# Optimal solution time complexity is O(1)
t = int(input())
for _ in range(t):
    n = int(input())
    if n & (n - 1):
        print("YES")
    else:
        print("NO")
