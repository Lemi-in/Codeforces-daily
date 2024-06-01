s = input().strip()
m = int(input().strip())
n = len(s)
prefix = [0] * n

for i in range(1, n):
    prefix[i] = prefix[i - 1]
    if s[i] == s[i - 1]:
        prefix[i] += 1

for _ in range(m):
    l, r = map(int, input().strip().split())
    l -= 1
    r -= 1
    print(prefix[r] - prefix[l])
