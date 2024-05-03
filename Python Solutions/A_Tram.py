n = int(input())
capacity = 0
enterExit = 0
for _ in range(n):
    a , b = map(int, input().split())
    enterExit += b - a
    capacity = max(capacity, enterExit)
print(capacity)
