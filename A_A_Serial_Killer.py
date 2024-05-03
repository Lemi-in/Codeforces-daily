v1 , v2 = map(str, input().split())
n = int(input())
print(v1, v2)
for _ in range(n):
    a, b = map(str, input().split())
    if a == v1:
        v1 = b
    else:
        v2 = b
    print(v1, v2)
