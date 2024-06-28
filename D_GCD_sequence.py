from math import gcd
from itertools import combinations

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    gcds = [gcd(a[i], a[i+1]) for i in range(n-1)]
    flag = False
    for i in range(n):
        if all(gcds[j] <= gcds[j+1] for j in range(i, n-2)) or all(gcds[j] <= gcds[j+1] for j in range(i+1, n-1)):
            flag = True
            break
    print("YES" if flag else "NO")