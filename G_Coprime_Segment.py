from math import gcd
from functools import reduce

def find(n, arr):
    l = 0
    curr = 0
    mn = float('inf')

    for r in range(n):
        curr = gcd(curr, arr[r])
        
        while curr == 1:
            mn = min(mn, r - l + 1)
            curr = reduce(gcd, arr[l+1:r+1], 0)  
            l += 1

    return mn if mn != float('inf') else -1


n = int(input())
arr = list(map(int, input().split()))


print(find(n, arr))
