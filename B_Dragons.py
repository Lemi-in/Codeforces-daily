s , n = map(int, input().split())

cha = []
for _ in range(n):
    x , y = map(int, input().split())
    cha.append((x , y))

cha.sort()

for x , y in cha:
    if s > x:
        s += y
    else:
        print('NO')
        exit()
print("YES")