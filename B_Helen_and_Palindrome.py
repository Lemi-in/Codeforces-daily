t = int(input())

for _ in range(t):
    s = input().strip()

    if s == s[0] * len(s):

        print(-1)
    else:
        print(len(s) - 1)
