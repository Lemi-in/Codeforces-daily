n = int(input())
litX = list(map(int, input().split()))
litY = list(map(int, input().split()))

levels = set()
for x in litX[1:]:
    levels.add(x)
for y in litY[1:]:
    levels.add(y)

if len(levels) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")