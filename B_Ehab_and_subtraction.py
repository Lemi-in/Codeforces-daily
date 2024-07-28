n, m = map(int, input().split())
s = list(map(int, input().split()))
s = set(s)
s.add(0)

s = sorted(s)
j = 0

for i in range(m):
    if j + 1 == len(s):
        print(0)
    else:
        print(s[j + 1] - s[j])
        j += 1
