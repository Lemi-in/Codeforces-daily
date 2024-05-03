n = int(input())
s = input()
f , r = 0 , 1
count = 0
while r < n:
    if s[f] == s[r]:
        count += 1
    f += 1
    r += 1
print(count)
