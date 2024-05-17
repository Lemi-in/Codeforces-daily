# Read the number of test cases
tt = int(input().strip())

for _ in range(tt):
    s = input().strip()
    res = 1
    ex = False

    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            res += 1
        if s[i] == '0' and s[i + 1] == '1':
            ex = True

    print(res - ex)
