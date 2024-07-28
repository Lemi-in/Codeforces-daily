def isEven (n):
    return n % 2 == 0
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)

    boo = True
    for i in range(n):
        if a[i] % 2 != b[i] % 2:
            boo = False
    if boo:
        print('YES')
    else:
        print('NO')