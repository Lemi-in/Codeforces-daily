n = int(input())
x_coords = set()
y_coords = set()
for _ in range(n):
    x, y = map(int, input().split())
    x_coords.add(x)
    y_coords.add(y)

res = 0
for x in x_coords:
    for y in y_coords:
        if (x, y) not in [(x, y) for _ in range(n) for x, y in [map(int, input().split())]]:
            res += 1

print(res)