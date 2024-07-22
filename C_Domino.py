

n = int(input())
s1, s2 = 0, 0
odd_upper, odd_lower = 0, 0
for _ in range(n):
    x, y = map(int, input().split())
    s1 += x
    s2 += y
    if x % 2 != y % 2:
        if x % 2 == 0:
            odd_upper += 1
        else:
            odd_lower += 1

if s1 % 2 == 0 and s2 % 2 == 0:
    print(0)
elif s1 % 2 != s2 % 2:
    print(-1)
elif odd_upper > 0 or odd_lower > 0:
    print(1)
else:
    print(-1)