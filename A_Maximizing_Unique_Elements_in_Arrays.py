t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a = set(a)
    m = len(a)
    if (n - m) % 2 == 0:
        print(m)
    else:
        print(m - 1)