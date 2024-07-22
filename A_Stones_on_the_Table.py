n = int(input())
s = input()
l , r = 0, 1
cnt = 0
while r < n:
    if s[l] == s[r]:
        cnt += 1
    r += 1
    l += 1
print(cnt)