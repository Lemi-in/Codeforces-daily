t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    counter = 0
    i = 0
    while i < len(s):
        if i + 2 < len(s) and (s[i:i+3] == 'pie' or s[i:i+3] == 'map'):
            counter += 1
            i += 3
        else:
            i += 1

    print(counter)
