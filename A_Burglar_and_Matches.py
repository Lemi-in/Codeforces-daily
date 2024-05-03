n, m = map(int, input().split())

stolen = 0
games = []
for i in range(m):
    a, b = map(int, input().split())
    games.append((a, b))


games.sort(key=lambda x: x[1], reverse=True)


for x , y in games:
    if n > 0:
        if n >= x:
            stolen += x * y
            n -= x
        else:
            stolen += n * y
            n = 0
    else:
        break

print(stolen)
