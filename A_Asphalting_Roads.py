n = int(input())
t = n * n

intersections = []
for _ in range(t):
    h, v = map(int, input().split())
    intersections.append((h, v))

x = set()
y = set()

days = []

for day in range(t):
    h, v = intersections[day]
    
    if h not in x and v not in y:
        x.add(h)
        y.add(v)
        days.append(day + 1)
print(*days)
