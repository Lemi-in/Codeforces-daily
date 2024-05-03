t = int(input())

for _ in range(t):
    s = input()
    wb = set()
    i = 0
    while i < len(s):
        if i == len(s) - 1 or s[i] != s[i + 1]:
            wb.add(s[i])
            i += 1
        else:
            i += 2
    print(''.join(sorted(wb)))
