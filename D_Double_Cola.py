n = int(input())
s = "Sheldon Leonard Penny Rajesh Howard".split()
i = 0
while n > 5 * 2 ** i:
    n -= 5 * 2 ** i
    i += 1
print(s[(n - 1) // 2 ** i])