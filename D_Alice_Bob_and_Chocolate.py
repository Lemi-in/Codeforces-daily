n = int(input())
a = list(map(int, input().split()))

alice , bob = 0, n - 1
asum , bsum = 0, 0
while alice <= bob:
    if asum <= bsum:
        asum += a[alice]
        alice += 1
    else:
        bsum += a[bob]
        bob -= 1
print(alice, n - alice)