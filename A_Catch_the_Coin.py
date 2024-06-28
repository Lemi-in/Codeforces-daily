n = int(input())
coins = []
for _ in range(n):
    x, y = map(int, input().split())
    if y >= -1:
        print("YES")
    else:
        print("NO")