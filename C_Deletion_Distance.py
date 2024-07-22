s = input()
t = input()
n = len(s)
m = len(t)

if s[n - 1] != t[m - 1]:
    print(n + m)
    exit()

i , j = n - 1 , m - 1
cnt = 0
while i >= 0 and j >= 0 and s[i] == t[j]:
    i -= 1
    j -= 1
print((i + 1) + (j + 1))

