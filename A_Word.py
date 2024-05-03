s = input()

lowCount = 0
upCount = 0
for char in s:
    if char.islower():
        lowCount += 1
    elif char.isupper():
        upCount += 1

if upCount > lowCount:
    print(s.upper())
else:
    print(s.lower())