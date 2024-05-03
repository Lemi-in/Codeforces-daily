s , n = map(int , input().split())
challenge = []
for _ in range(n):
    x , y = map(int, input().split())
    challenge.append((x, y))
challenge.sort()
for x , y in challenge:
    if s > x:
        s += y
    else:
        print("NO")
        break
else:
    print("YES")