t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    max_factors = 0
    for i in range(l, r + 1):
        factors = 0
        j = 2
        while j * j <= i:
            if i % j:
                j += 1
            else:
                i //= j
                factors += 1
        if i > 1:
            factors += 1
        max_factors = max(max_factors, factors)
    print(max_factors)