c, d = input()

if c == 'a' or c == 'h':
    cnt = 1
else:
    cnt = 0
if d == '1' or d == '8':
    cnt += 1

if cnt == 0:
    print(8)
elif cnt == 1:
    print(5)
elif cnt == 2:
    print(3)
else:
    raise Exception("Invalid input")