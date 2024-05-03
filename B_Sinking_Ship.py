n = int(input())

rats = []
WnC = []
men = []
cap = ''

for _ in range(n):
    name, id = input().split()
    if id == 'rat':
        rats.append(name)
    elif id == 'woman' or id == 'child':
        WnC.append(name)
    elif id == 'man':
        men.append(name)
    else:
        cap = name

for name in rats:
    print(name)
for name in WnC:
    print(name)
for name in men:
    print(name)
print(cap)
