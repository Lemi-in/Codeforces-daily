f, s = map(int, input().split())
minutes= 0

while f > 0 and s > 0 and not (f == 1 and s == 1):
    if f > s:
        f, s = s, f 
    f += 1
    s -= 2
    minutes += 1
print(minutes)

