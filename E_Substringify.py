n = int(input())
s = [input() for _ in range(n)]

s.sort(key=lambda x: len(x))

for i in range(n - 1):
    if s[i + 1].find(s[i]) == -1:
        print("NO")
        exit()

print("YES")
for char in s:
    print(char)

