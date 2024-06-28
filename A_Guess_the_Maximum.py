t= int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    an = []
    for i in range(n - 1):
        an.append(max(arr[i], arr[i + 1]))
    print(sorted(an)[0] - 1)
